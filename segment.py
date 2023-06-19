import cv2 as cv
import time
import numpy as np
import argparse
import os
import time
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from models.experimental import attempt_load
from utils.datasets import letterbox
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized


parser = argparse.ArgumentParser()
parser.add_argument('--weights', nargs='+', type=str, default='runs/train/exp7/weights/best.pt', help='model.pt path(s)')#选择模型的版本、大小
parser.add_argument('--source', type=str, default='0', help='source')  # file/folder for singel frame, 0 for webcam
parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')#图片中间处理过程中的大小，最后会等比例放大成和原图一模一样
parser.add_argument('--conf-thres', type=float, default=0.75, help='object confidence threshold')#显示图片置信度控制 default=0.25
parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')#IOU：交并比 NMS：非极大值抑制（多个框中找置信度最大的框）（目的是为了避免重复判断，或者把两个物体判断为一个）（这里大于default我们才把几个框合并成一个框）default=0.45
parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
parser.add_argument('--view-img', action='store_true', help='display results')
parser.add_argument('--save-txt', action='store_true',default=True, help='save results to *.txt')
parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
parser.add_argument('--augment', action='store_true', help='augmented inference')
parser.add_argument('--update', action='store_true', help='update all models')
parser.add_argument('--project', default='runs/detect', help='save results to project/name')
parser.add_argument('--name', default='exp', help='save results to project/name')
parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
parser.add_argument('--hide-labels', default=True, action='store_true', help='hide labels')
parser.add_argument('--hide-conf', default=True, action='store_true', help='hide confidences')
opt = parser.parse_args()

def readTxt(path):
    data = []
    with open(path,"r") as f:
        for line in f.readlines():
            line = line.strip("\n")
            line = line.split()
            data.append(line)
    #print(data)
    return data
def get_labels():
    HEIGHT = 480 #y
    WIDTH = 640 #x

    f_path='labels'
    f_name=os.listdir(f_path)
    count=0
    x=[]
    y = []
    w = []
    h = []
    n = []
    for f in f_name:
        path=f_path+'/'+f
        a=readTxt(path)
        x.append([])
        y.append([])
        w.append([])
        h.append([])
        for i in range(0,len(a)):
            # x[count].append(float(a[i][1]))
            # y[count].append(float(a[i][2]))
            # w[count].append(float(a[i][3]))
            # h[count].append(float(a[i][4]))
            x[count].append(round(float(a[i][1])*WIDTH))
            y[count].append(round(float(a[i][2])*HEIGHT))
            w[count].append(round(float(a[i][3])*WIDTH))
            h[count].append(round(float(a[i][4])*HEIGHT))
        n.append(len(a)) #一帧检测出的物体个数
        count = count + 1
    return n,x,y,w,h #n为检测出的目标数，x,y为中心点的坐标，w，h为宽度和高度（以yolov5官方定义的标准）

def get_labels1(path):
    HEIGHT = 480 #y
    WIDTH = 640 #x
    x=[]
    y = []
    w = []
    h = []
    n = []
    a = readTxt(path)
    for i in range(0,len(a)):
        # x[count].append(float(a[i][1]))
        # y[count].append(float(a[i][2]))
        # w[count].append(float(a[i][3]))
        # h[count].append(float(a[i][4]))
        x.append(round(float(a[i][1])*WIDTH))
        y.append(round(float(a[i][2])*HEIGHT))
        w.append(round(float(a[i][3])*WIDTH))
        h.append(round(float(a[i][4])*HEIGHT))
    n.append(len(a)) #一帧检测出的物体个数

    return n,x,y,w,h #n为检测出的目标数，x,y为中心点的坐标，w，h为宽度和高度（以yolov5官方定义的标准）

def segment(image):
    source, weights, view_img, save_txt, imgsz = opt.source, opt.weights, opt.view_img, opt.save_txt, opt.img_size
    source='img'
    # Python endswith() 方法用于判断字符串是否以指定后缀结尾
    save_img = not opt.nosave and not source.endswith('.txt')  # save inference images

    # 判断source字符是否全部由字符组成或有特定的前后缀
    webcam = source.isnumeric() or source.endswith('.txt') or source.lower().startswith(
        ('rtsp://', 'rtmp://', 'http://', 'https://'))

    # Directories
    save_dir = Path(increment_path(Path(opt.project) / opt.name, exist_ok=opt.exist_ok))  # increment run
    (save_dir / 'labels' if save_txt else save_dir).mkdir(parents=True, exist_ok=True)  # make dir

    # Initialize
    HEIGHT = 480  # y
    WIDTH = 640  # x
    set_logging()
    device = select_device(opt.device)
    half = device.type != 'cpu'  # half precision only supported on CUDA
    last_txt_path = '0'

    # Load model
    model = attempt_load(weights, map_location=device)  # load FP32 model
    stride = int(model.stride.max())  # model stride
    imgsz = check_img_size(imgsz, s=stride)  # check img_size
    if half:
        model.half()  # to FP16

    # Second-stage classifier
    classify = False
    if classify:
        modelc = load_classifier(name='resnet101', n=2)  # initialize
        modelc.load_state_dict(torch.load('weights/resnet101.pt', map_location=device)['model']).to(device).eval()



    # Get names and colors
    names = model.module.names if hasattr(model, 'module') else model.names
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]

    # Run inference
    if device.type != 'cpu':
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  # run once
    t0 = time.time()



    img0=image
    image_size=640
    img = letterbox(img0, image_size, stride=32)[0]

    # Convert
    img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
    img = np.ascontiguousarray(img)
    
    img = torch.from_numpy(img).to(device)
    img = img.half() if half else img.float()  # uint8 to fp16/32
    img /= 255.0  # 0 - 255 to 0.0 - 1.0
    if img.ndimension() == 3:
        img = img.unsqueeze(0)

    # Inference
    t1 = time_synchronized()
    pred = model(img, augment=opt.augment)[0]

    # Apply NMS
    pred = non_max_suppression(pred, opt.conf_thres, opt.iou_thres, classes=opt.classes, agnostic=opt.agnostic_nms)
    t2 = time_synchronized()

    # Apply Classifier
    if classify:
        pred = apply_classifier(pred, modelc, img, img0)

    # Process detections
    for i, det in enumerate(pred):  # detections per image
        s, im0,  = '', img0



        ####################################保存实时检测图片################################
        # pic_dir = str(save_dir) + '/pic'
        # if not os.path.exists(pic_dir):
        #     os.makedirs(pic_dir)
        # pic_path = pic_dir + '\\' + str(p.stem) + ('' if dataset.mode == 'image' else f'_{frame}')
        ##################################################################################

        s += '%gx%g ' % img.shape[2:]  # print string
        gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
        if len(det):
            # Rescale boxes from img_size to im0 size
            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

            # Print results
            for c in det[:, -1].unique():
                n = (det[:, -1] == c).sum()  # detections per class
                s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string
                # print(f'{n}')
            # Write results
            x_list = []
            y_list = []
            w_list = []
            h_list = []
            for *xyxy, conf, cls in reversed(det):
                if save_txt:  # Write to file
                    xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                    line = (cls, *xywh, conf) if opt.save_conf else (cls, *xywh)  # label format
                    x3 = round(xywh[0] * WIDTH)
                    y3 = round(xywh[1] * HEIGHT)
                    w3 = round(xywh[2] * WIDTH)
                    h3 = round(xywh[3] * HEIGHT)
                    with open(txt_path + '.txt', 'a') as f:
                        # print(x3,y3,w3,h3)
                        x_list.append(x3)
                        y_list.append(y3)
                        w_list.append(w3)
                        h_list.append(h3)
                        f.write(('%g ' * len(line)).rstrip() % line + '\n')
                if save_img or view_img:  # Add bbox to image
                    label = ''  # f'{names[int(cls)]} {conf:.2f}'#不显示标签和置信度了
                    plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=3)

            # print(x_list,y_list,w_list,h_list)
            yield f'{n}', x_list, y_list, w_list, h_list
            print()  # 每一帧数据空一一行
            ##############################只保存含目标的实时检测图片#################################
            # pic = (int(xyxy[0].item()) + int(xyxy[2].item())) / 2
            # if pic != 0:
            #     cv2.imwrite(pic_path + f'{p.stem}.jpg', im0)
            # else:
            #     im1 = cv2.imread('no.jpg', 1)
            #     cv2.imwrite(pic_path + f'{p.stem}.jpg', im1)
            #####################################################################################

        # Print time (inference + NMS)
        # print(f'{s}Done. ({t2 - t1:.3f}s)')
        # print(f'{n}') #输出识别到的项目个数



    # n1, x1, y1, w1, h1 = get_labels1(txt_path)  # 得到实时的label
    # print(n1)
    # print(txt_path.split('\\'))
    # txt_path_list=txt_path.split('\\')
    # last_txt_path=txt_path_list[0]+'/'+txt_path_list[1]+'/'+txt_path_list[2]+'/'+txt_path_list[3]+'/'+txt_path_list[4]+'.txt'
    # print(last_txt_path)
    # if os.path.exists(last_txt_path):
    #     n1, x1, y1, w1, h1 = get_labels1(last_txt_path)  # 得到实时的label
    #     print(n1)
    #     print(x1)
    #     print(y1)
    #     print(w1)
    #     print(h1)
    # if save_txt or save_img:
    #     s = f"\n{len(list(save_dir.glob('labels/*.txt')))} labels saved to {save_dir / 'labels'}" if save_txt else ''
    #     print(f"Results saved to {save_dir}{s}")

    # print(f'Done. ({time.time() - t0:.3f}s)')

    # return n1,x1,y1,w1,h1
    return image


if __name__ =='__main__':
    # cap0=cv.VideoCapture('../images/expressions.mp4',0)#视频demo
    #获取摄像头序号可参考https://huaweicloud.csdn.net/63806dc3dacf622b8df882d9.html
    cap1 = cv.VideoCapture(0)#俯视摄像头，(1080, 1920, 3)
    # cap1_small=cv.VideoCapture(1)#俯视摄像头，(480, 640, 3)
    # cap2=cv.VideoCapture(2)#侧拍摄像头，(480, 640, 3)

    HEIGHT = 480
    WIDTH = 640
    cap1.set(cv.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap1.set(cv.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    # cap_0.set(5, FPS)# 帧率
    # cap2.set(cv.CAP_PROP_FRAME_WIDTH, WIDTH)
    # cap2.set(cv.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    # cap_1.set(5, FPS)# 帧率
    # for i in range(1,2001):
    while True:
        t = time.time()
        ret, frame = cap1.read()
        frame = cv.flip(frame, -1)
        # print(np.array(frame).shape)#获取帧大小
        # print('第{}帧'.format(i))
        image=segment(frame)
        # cv.namedWindow('all', cv.WINDOW_NORMAL)
        cv.imshow('all', image)
        print('运行1帧的时间为{:.2f}s'.format(time.time() - t))
        #点击esc或者x退出
        if cv.waitKey(1) == 27 or cv.getWindowProperty('all', 0) == -1:#ESC的ASCII码
            break

    cap1.release()
    # cap1_small.release()
    # cap2.release()
    cv.destroyAllWindows()
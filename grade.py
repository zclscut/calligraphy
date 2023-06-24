import cv2 as cv
import time

import numpy as np

from segment import segment
# import numpy as np
import torchvision.transforms as transforms
from torchvision.transforms import functional
import torch
import timm

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from PIL import Image

#正方形填充参考https://blog.csdn.net/u013685264/article/details/126520678
def square(image):
    # print('np.array(image).shape={}'.format(image.shape))
    (h, w, c) = image.shape
    max_wh = np.max([w, h])
    wp = int((max_wh - w) / 2)#width
    hp = int((max_wh - h) / 2)#height
    # print('wp={},hp={}'.format( wp ,hp))
    padding = (wp, hp, max_wh-w-wp, max_wh-h-hp)
    # print('padding={}'.format(padding))
    # padding: 设置填充大小
    # 当为a时，上下左右均填充a个像素
    # 当为(a, b)
    # 时，上下填充b个像素，左右填充a个像素
    # 当为(a，b，c，d)时，左，上，右，下分别填充a，b，c，d
    return transforms.Pad(padding, fill=0, padding_mode='constant')(Image.fromarray(image))

size=224
compose = transforms.Compose([
            # transforms.CenterCrop(224),
            transforms.Resize(size),
            transforms.ToTensor(),
            # transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])


# 看你是那种保存的模型
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# weights_path = "xception_64.18%.pth"
weights_path = 'xception_224.pth'
model = timm.create_model('xception41p', num_classes=5)
model.to(device)
model.load_state_dict(torch.load('lib/' + weights_path,map_location='cuda:0'))


def grade(frame,is_sort=True):
    frame, seg_list = segment(frame,is_sort)
    grade_list=[]
    image=frame

    HEIGHT = frame.shape[0]  # y
    WIDTH = frame.shape[1]  # x
    print('帧尺寸为{}'.format(frame.shape))

    print(seg_list)
    # seg_list=[[6],[352, 340, 417, 419, 423, 346],
    # [195, 388, 298, 386, 205, 287],
    # [60, 65, 53, 81, 68, 59],
    # [81, 102, 63, 79, 91, 72]]
    num_ch = seg_list[0][0]
    padding=0
    if num_ch:
        padding = np.max([np.max(np.array(seg_list[3])), np.max(np.array(seg_list[4]))])
    print('padding={} in grade.py'.format(padding))
    
    # frame_gray=frame
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    print('灰度化后帧尺寸为{}'.format(frame_gray.shape))
    # frame_gray = np.expand_dims(frame_gray, axis=2)
    # frame_gray = np.concatenate((frame_gray, frame_gray, frame_gray), axis=-1)
    frame_gray = cv.cvtColor(frame_gray, cv.COLOR_GRAY2BGR)
    print('灰度化后帧尺寸为{}'.format(frame_gray.shape))
    frame_gray=cv.copyMakeBorder(frame_gray, padding, padding, padding, padding, cv.BORDER_CONSTANT)
    print('padding后帧尺寸为{}'.format(frame_gray.shape))

    # plt.figure('padding')
    # plt.imshow(np.array(frame_gray))
    # plt.show()



    #对每一个汉字进行评分
    for i in range(num_ch):
        x,y,w,h=seg_list[1][i],seg_list[2][i],seg_list[3][i],seg_list[4][i]
        # print('x={},y={},w={},h={} center point'.format(x,y,w,h))

        max_wh = np.max([w, h])
        x=int(x-max_wh/2)
        y=int(y-max_wh/2)
        # print('x={},y={},w={},h={} left top point'.format(x, y, w, h))

        # character=Image.new('RGB', (max_wh, max_wh))#创建全0图像
        # plt.figure('character')
        # plt.imshow(character)
        # plt.show()

        # character=np.zeros([max_wh,max_wh,3],dtype=np.float32)
        # print('character.shape={} after init'.format(character.shape))
        # print('character.slice={} before cut'.format(character[100, 100:100 + 20, 1]))
        # # #从灰度化的图中截取汉字
        # y_cut=np.min([y+max_wh,HEIGHT])-y
        # x_cut=np.min([x+max_wh,WIDTH])-x
        # if x_cut<max_wh and y_cut<max_wh:
        #     character[0:y_cut,0:x_cut]=frame_gray[y:y+y_cut,x:x+x_cut]#opencv和yolov的x对应width,y对应height,而ndarray的h在前
        # # character = Image.fromarray(character)

        # padding=0
        y_cut=y+padding
        x_cut=x+padding
        character = frame_gray[y_cut:y_cut + max_wh, x_cut:x_cut + max_wh]
        # print('character.slice={} after gray'.format(character[100,100:100+20,1]))
        character = Image.fromarray(character)

        print('character={} after insert yolov seg'.format(np.array(character).shape))
        print('character.slice={}'.format(np.array(character)[50, 50:50 + 10, 1]))


        # print('image.shape={} before transform'.format(np.array(image).shape))
        print('image.shape={} before transform'.format(np.array(character).shape))
        # character=square(character)
        # print('image.shape={} after square'.format(np.array(character).shape))
        character = compose(character)
        # character=transforms.Pad([105, 105], fill=0, padding_mode='constant')(character)
        print('image.shape={} after transform'.format(np.array(character).shape))

        # cv.imshow('all', np.array(character.permute(1,2,0),dtype=np.float32))
        # cv.waitKey(0)


        print('character.slice={}'.format(character.permute(1,2,0)[50, 50:50 + 10, 1]))
        # plt.figure('character')
        # plt.imshow(np.array(character.permute(1,2,0),dtype=np.float32))#.astype('uint8')
        # plt.show()

        # print('image.shape={} after transform'.format(np.array(image).shape))
        character = torch.reshape(character, (1, 3, size, size))


        cha_grade=0
        model.eval()
        with torch.no_grad():
            character=character.to(device)
            out = model(character)
            cha_grade = out.argmax(1).item() + 1
            # print('out={} in grade function in grade.py'.format(out))
            # print('out.argmax(1)={} in grade function in grade.py'.format(out.argmax(1).item()))
            grade_list.append(cha_grade)
            print('图片预测为{}'.format(cha_grade))
        # grade_list = ['很差', '差', '一般', '好', '很好']
        grade_print_list = ['1', '2', '3', '4', '5']
        # print('图片预测为{}'.format(grade_list[cha_grade-1]))

        cv.rectangle(image, (x,y), (x+w,y+h), (0, 255, 0), 2)
        font = cv.FONT_HERSHEY_SIMPLEX  # 定义字体
        image = cv.putText(image, '{}'.format(grade_print_list[cha_grade-1]), (x,y-10), font, 2, ( 0, 0,255), 4)

    seg_list.append(grade_list)
    # print(seg_list)
    return image,seg_list



def cam_test():
    # cap0=cv.VideoCapture('../images/expressions.mp4',0)#视频demo
    # 获取摄像头序号可参考https://huaweicloud.csdn.net/63806dc3dacf622b8df882d9.html
    cap1 = cv.VideoCapture(0)  # 俯视摄像头，(1080, 1920, 3)
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
        image, grade_list = grade(frame, is_sort=False)
        print('grade_list={}'.format(grade_list[-1]))
        # cv.namedWindow('all', cv.WINDOW_NORMAL)
        cv.imshow('all', image)
        print('运行1帧的时间为{:.2f}s'.format(time.time() - t))
        # 点击esc或者x退出
        if cv.waitKey(1) == 27 or cv.getWindowProperty('all', 0) == -1:  # ESC的ASCII码
            break

    cap1.release()
    # cap1_small.release()
    # cap2.release()
    cv.destroyAllWindows()

def pic_test(image_path):
    # image_path='img/2.jpg'

    frame = cv.imread(image_path)

    t = time.time()

    # print(np.array(frame).shape)#获取帧大小
    # print('第{}帧'.format(i))
    image, grade_list = grade(frame, is_sort=False)
    print('grade_list={}'.format(grade_list[-1]))
    # cv.namedWindow('all', cv.WINDOW_NORMAL)
    cv.imshow('all', image)
    print('运行1帧的时间为{:.2f}s'.format(time.time() - t))
    cv.waitKey(0)
    if cv.waitKey(1) == 27 or cv.getWindowProperty('all', 0) == -1:  # ESC的ASCII码
        cv.destroyAllWindows()



if __name__ =='__main__':
    cam_test()

    # image_path = 'img/5.jpg'
    # pic_test(image_path)
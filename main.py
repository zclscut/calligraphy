import cv2 as cv
import numpy as np
import time
#龚圣杰握笔姿势检测
from penhold import *
#钟晋握笔力度检测
from penforce import *
#单泽昱文字分割
from segment import *
#余思进文字转语音
from audio import *
from grade import *
from sitpos import *

if __name__ =='__main__':
    # cap0=cv.VideoCapture('../images/expressions.mp4',0)#分析视频demo表情
    cap1 = cv.VideoCapture(0)#俯视摄像头，(1080, 1920, 3)
    cap1_small=cv.VideoCapture(1)#俯视摄像头，(480, 640, 3)
    cap2=cv.VideoCapture(2)#侧拍摄像头，(480, 640, 3)

    HEIGHT = 480
    WIDTH = 640
    cap1.set(cv.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap1.set(cv.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    # cap_0.set(5, FPS)# 帧率
    cap2.set(cv.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap2.set(cv.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    # cap_1.set(5, FPS)# 帧率
    # for i in range(1,2001):
    while True:
        t = time.time()
        # 以下设置显示屏的宽高

        ret1, frame1 = cap1_small.read()
        ret2,frame2= cap2.read()
        # print('the shape of frame 1 is {}'.format(np.array(cv.resize(frame1, (HEIGHT,WIDTH))).shape))
        # print('the shape of frame 2 is {}'.format(np.array(cv.resize(frame2, (HEIGHT,WIDTH))).shape))
        # print('获取帧时间{:.2f}s'.format(time.time() - t))
        # t = time.time()
        if not ret1:
            print('摄像头1未打开')
        elif not ret2:
            print('摄像头2未打开')
        else:
            frame2=penhold(frame2)
            frame2 = penforce(frame2)
            frame2 = sitpos(frame2)
            frame1 = cv.flip(frame1, -1)
            frame1=grade(frame1)

            frame=np.concatenate((cv.resize(frame1, (WIDTH, HEIGHT)),cv.resize(frame2, (WIDTH, HEIGHT))),axis=1)
            # print('concat时间{:.2f}s'.format(time.time() - t))
            # t = time.time()
            # print(np.array(frame).shape)#获取帧大小
            # print('第{}帧'.format(i))
            image=frame
            # cv.namedWindow('all', cv.WINDOW_NORMAL)
            cv.imshow('all', image)
            print('运行1帧的时间为{:.2f}s'.format(time.time() - t))

        #点击esc或者交叉退出
        if cv.waitKey(1) == 27 or cv.getWindowProperty("all",cv.WND_PROP_AUTOSIZE) != 1:#ESC的ASCII码
            break

    cap1.release()
    cap1_small.release()
    cap2.release()
    cv.destroyAllWindows()


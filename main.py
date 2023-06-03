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

if __name__ =='__main__':
    # cap0=cv.VideoCapture('../images/expressions.mp4',0)#分析视频demo表情
    cap1 = cv.VideoCapture(0)#俯视摄像头，(1080, 1920, 3)
    cap1_small=cv.VideoCapture(1)#俯视摄像头，(480, 640, 3)
    cap2=cv.VideoCapture(2)#侧拍摄像头，(480, 640, 3)
    # for i in range(1,2001):
    while True:
        # t = time.time()
        ret, frame = cap1.read()
        print(np.array(frame).shape)#获取帧大小
        # print('第{}帧'.format(i))
        image=frame
        # cv.namedWindow('all', cv.WINDOW_NORMAL)
        cv.imshow('all', image)
        # print('运行1帧的时间为{:.2f}s'.format(time.time() - t))
        #点击esc或者交叉退出
        if cv.waitKey(1) == 27 or cv.getWindowProperty("all",cv.WND_PROP_AUTOSIZE) != 1:#ESC的ASCII码
            break

    cap1.release()
    cv.destroyAllWindows()


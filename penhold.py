import cv2 as cv
import time
import numpy as np



def penhold(image):

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
        # print(np.array(frame).shape)#获取帧大小
        # print('第{}帧'.format(i))
        image=penhold(frame)
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
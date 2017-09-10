import robo
import cv2
from test import RoboCV
import threading
import numpy as np

weixin_temp1 = cv2.imread('hong1.png',0)
weixin_temp2 = cv2.imread('hong2.png',0)
w1, h1 = weixin_temp1.shape[::-1]
w2, h2 = weixin_temp2.shape[::-1]

def screenUpdated(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(img_gray, weixin_temp1, cv2.TM_CCOEFF_NORMED)
    threshold = 0.85
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w1, pt[1] + h1), (0, 0, 255), 2)

    res = cv2.matchTemplate(img_gray, weixin_temp2, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w2, pt[1] + h2), (0, 255, 0), 2)

    cv2.imshow('weixin1', img)

class UnlockThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.unlock()

    def unlock(self):
        robo.strongPush(200,50)
        robo.strongPush(200,50)
        robo.unlock('1', '5', '9', '3', '5', '7')

if __name__ == '__main__':
    cv = RoboCV()
    UnlockThread().start()
    cv.execute(screenUpdated)
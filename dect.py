import cv2
import numpy as np

cap = cv2.VideoCapture(1)

template = cv2.imread('crop.jpg')
temp_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

while(1):

    # Take each frame
    _, frame = cap.read()

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Initiate SIFT detector
    sift = cv2.SIFT()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img_gray,None)
    kp2, des2 = sift.detectAndCompute(temp_gray,None)

    # BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2, k=2)

    # Apply ratio test
    good = []
    for m,n in matches:
        if m.distance < 0.25*n.distance:
            good.append([m])

    # cv2.drawMatchesKnn expects list of lists as matches.
    img3 = cv2.drawMatchesKnn(frame,kp1,template,kp2,good,frame,flags=2)
    cv2.imshow('result',img3)

    # cv2.imshow('frame',frame)
    # cv2.imshow('mask',mask)
    # cv2.imshow('edges', edges)
    # cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
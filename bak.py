import cv2
import numpy as np

cap = cv2.VideoCapture(0)

found = False
captured = False
lower_black = np.array([0, 0, 0])
upper_black = np.array([255, 64, 255])
mask = None
edged = None
points = []

while(1):

    # Take each frame
    _, frame = cap.read()

    if not found:

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(frame, lower_black, upper_black)

        res = cv2.bitwise_and(frame, frame, mask=mask)

        w, h = mask.shape

        if np.count_nonzero(mask) > w * h / 9:
            found = True

        cv2.imshow('frame',frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res',res)
    elif not captured:
        res = frame.copy()
        edged = cv2.Canny(mask, 100, 200)
        cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
        # print cnts


        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            if len(approx) == 4:
                points = approx
                cv2.drawContours(res, [approx], -1, (0, 255, 0), 3)
                break
        
        cv2.imshow('frame',frame)
        cv2.imshow('canny', edged)
        cv2.imshow('mask', mask)
        cv2.imshow('res',res)

        if cv2.contourArea(points) > 10000:
            captured = True
        else:
            found = False
    else:
        pts1 = np.float32(points)
        pts2 = np.zeros_like(pts1)

        w, h, c = frame.shape

        w_mean = np.mean(pts1[:,:,0])
        h_mean = np.mean(pts1[:,:,1])

        for i, point in enumerate(points):
            p = point[0]

            # left bottom
            if p[0] < w_mean and p[1] > h_mean:
                pts2[i, 0, :] = [0, 0]
            elif p[0] < w_mean and p[1] < h_mean: #left top
                pts2[i, 0, :] = [w, 0]
            elif p[0] > w_mean and p[1] > h_mean: #right bottom
                pts2[i, 0, :] = [0, h]
            elif p[0] > w_mean and p[1] < h_mean: #right top
                pts2[i, 0, :] = [w, h]


        M = cv2.getPerspectiveTransform(pts1, pts2)

        phone = cv2.warpPerspective(frame, M, (w, h))
        cv2.drawContours(frame, [approx], -1, (0, 255, 0), 3)
        cv2.imshow('frame',frame)
        cv2.imshow('canny', edged)
        cv2.imshow('phone', phone)

        captured = False
        mask = frame.copy()



    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

def screenUpdated():
    pass
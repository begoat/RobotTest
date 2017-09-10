import cv2
import numpy as np

class RoboCV(object):

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.found = False
        self.captured = False
        self.lower_black = np.array([0, 0, 0])
        self.upper_black = np.array([255, 127, 255])
        self.mask = None
        self.edged = None
        self.points = []

    def execute(self, onUpdate):
        while(1):

            # Take each frame
            _, frame = self.cap.read()

            if not self.found:

                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

                mask = cv2.inRange(frame, self.lower_black, self.upper_black)

                res = cv2.bitwise_and(frame, frame, mask=mask)

                w, h = mask.shape

                if np.count_nonzero(mask) > w * h / 9:
                    self.found = True

                cv2.imshow('frame',frame)
                cv2.imshow('mask', mask)
                cv2.imshow('res',res)
            elif not self.captured:
                res = frame.copy()
                edged = cv2.Canny(mask, 100, 200)
                cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]
                cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
                # print cnts


                for c in cnts:
                    peri = cv2.arcLength(c, True)
                    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
                    if len(approx) == 4:
                        self.points = approx
                        cv2.drawContours(res, [approx], -1, (0, 255, 0), 3)
                        break
                
                cv2.imshow('frame',frame)
                cv2.imshow('canny', edged)
                cv2.imshow('mask', mask)
                cv2.imshow('res',res)

                if cv2.contourArea(self.points) > 10000:
                    self.captured = True
                else:
                    self.found = False
            else:
                pts1 = np.float32(self.points)
                pts2 = np.zeros_like(pts1)

                w, h, c = frame.shape

                w_mean = np.mean(pts1[:,:,0])
                h_mean = np.mean(pts1[:,:,1])

                for i, point in enumerate(self.points):
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

                # captured = False
                # mask = frame.copy()

                res = cv2.warpPerspective(frame, M, (w, h))
                cv2.drawContours(frame, [approx], -1, (0, 255, 0), 3)
                cv2.imshow('frame',frame)
                cv2.imshow('canny', edged)
                cv2.imshow('res', res)

                onUpdate(res)

            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break

        cv2.destroyAllWindows()
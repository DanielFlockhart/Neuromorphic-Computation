import pyautogui,cv2,time
import cv2
from PIL import Image,ImageGrab
import numpy as np
from threading import Thread

class Eye:
    def __init__(self,fps=30):
        self.fps = fps
        self.name = 'eye'
        self.type = 'sensor'
        self.status = 'functional'
        self.video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.output = []

    def get_status(self):
        return self.status

    def getMatrix(self, img):
        data = np.asarray( img, dtype="int32" )
        data = data.flatten()
        data = [point/255 for point in data]
        return data
    def getOutput(self):
        return self.output



class Webcam(Eye):
    def __init__(self, fps=30):
        super().__init__(fps)

    def convertImage(self,frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (16,16), fx = 1, fy = 1)
        return frame 

    def run(self):
        ret, frame = self.video.read()
        frame = self.convertImage(frame)
        self.output = self.getMatrix(frame)


class Screen(Eye):
    def __init__(self, fps=30):
        super().__init__(fps)

    def run(self):
        img = ImageGrab.grab()
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        frame = cv2.resize(frame, (16,16), fx = 1, fy = 1)
        self.output = self.getMatrix(frame)



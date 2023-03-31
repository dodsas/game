from enum import Enum
import image_finder
import image_clicker
import dun_print
import cv2
import image_keyboard

class Actionable:
    def action(self):
        pass

class Clicker:
    def __init__(self, imageName: str, threshold: float=0.93, screenShot: cv2.Mat=None, errorMode=False):
        self.imageName = imageName 
        self.threshold = threshold 
        self.screenShot = screenShot
        self.errorMode = errorMode

    def action(self):
        pt, score = image_finder.find(self.imageName, screenShot=self.screenShot, threshold=self.threshold)
        if pt is None:
            dun_print.printf(self.imageName, 'NOT_FOUND', f'{score:.4f}')
            if self.errorMode:
                dun_print.errorf(self.imageName)
        else: 
            image_clicker.click(pt)
            dun_print.printf(self.imageName, 'FOUND', f'{score:.4f}', f'x:{pt[0]} y:{pt[1]}')

class Presser:
    def __init__(self, key: str):
        self.key = key 
    def action(self):
        image_keyboard.press(self.key)
        dun_print.printf('KEY PRESS', self.key)


# action = Clicker('test')
# action.action()
# action = Presser('ESC')
# action.action()
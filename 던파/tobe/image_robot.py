from enum import Enum
import time
import image_finder
import image_clicker
import dun_print
import cv2
import image_keyboard

g_fallbackCount = 15
g_skipCount = 4
g_prevAction = None

class Actionable:
    def action(self, printFail=False, printOk=True, screenShot=None):
        pass
    def name(self):
        pass
    def fallback(self, screenShot=None):
        pass

class Founder(Actionable):
    def __init__(self, imageName: str, threshold: float=0.93, screenShot: cv2.Mat=None, errorMode=False):
        self.imageName = imageName 
        self.threshold = threshold 
        self.screenShot = screenShot
        self.errorMode = errorMode

    def action(self, printFail=False, printOk=True, screenShot=None):
        if screenShot is not None:
            self.screenShot = screenShot

        pt, score = image_finder.find(self.imageName, screenShot=self.screenShot, threshold=self.threshold)
        if pt is None:
            if printFail:
                dun_print.printf(self.imageName, 'NOT_FOUND', f'{score:.4f}')
            if self.errorMode:
                dun_print.errorf(self.imageName)
            return False
        else: 
            if printOk:
                dun_print.printf(self.imageName, 'FOUND', f'{score:.4f}', f'x:{pt[0]} y:{pt[1]}')
            return True
    
    def fallback(self, screenShot=None):
        time.sleep(0.2)
        self.action(printFail=True, printOk=True, screenShot=screenShot)

    def name(self):
        return self.imageName

class Clicker(Actionable):
    def __init__(self, imageName: str, threshold: float=0.90, screenShot: cv2.Mat=None, errorMode=False):
        self.imageName = imageName 
        self.threshold = threshold 
        self.screenShot = screenShot
        self.errorMode = errorMode

    def action(self, printFail=False, printOk=True, screenShot=None):
        if screenShot is not None:
            self.screenShot = screenShot

        pt, score = image_finder.find(self.imageName, screenShot=self.screenShot, threshold=self.threshold)
        if pt is None:
            if printFail:
                dun_print.printf(self.imageName, 'NOT_CLICK', f'{score:.4f}')
            if self.errorMode:
                dun_print.errorf(self.imageName)
            return False
        else: 
            image_clicker.click(pt)
            if printOk:
                dun_print.printf(self.imageName, 'CLICK', f'{score:.4f}', f'x:{pt[0]} y:{pt[1]}')
            return True
    
    def fallback(self, screenShot=None):
        time.sleep(0.2)
        self.action(printFail=True, printOk=True, screenShot=screenShot)

    def name(self):
        return self.imageName

class Presser(Actionable):
    def __init__(self, key: str):
        self.key = key 

    def action(self, printFail=False, printOk=True, screenShot=None):
        if screenShot is not None:
            self.screenShot = screenShot

        image_keyboard.press(self.key)
        if printOk:
            dun_print.printf('KEY PRESS', self.key)
        time.sleep(2)
        return True

    def fallback(self, screenShot=None):
        time.sleep(3)
        self.action(printFail=False, printOk=False, screenShot=screenShot)     

    def name(self):
        return self.key

def action(currAction: Actionable, canSkip=False):
    global g_prevAction
    global g_fallbackCount
    global g_skipCount

    loopCount = 0
    isOk = False
    # dun_print.printf(currAction.name(), 'START')

    while True:
        screenShot = image_finder.getScreenShotToGray()
        # skip
        Clicker('확인', screenShot=screenShot).action(printFail=False)

        if canSkip and loopCount == g_skipCount:
            currAction.action(printFail=True, screenShot=screenShot)
            break
        if loopCount == g_fallbackCount:
            currAction.action(printFail=True, screenShot=screenShot)
            dun_print.errorf(currAction.name())
        if currAction.action() is True:
            isOk = True
            break
        else:
            loopCount += 1
            if g_prevAction is not None:
                g_prevAction.fallback(screenShot=screenShot)

    if canSkip == False :
        g_prevAction = currAction
    
    return isOk

# action(Clicker('상점', threshold=0.78))
# action(Clicker('상점_상점'))

# # 자질구리한 팝업 스킵
# screenshot = image_finder.getScreenShotToGray()
# Clicker('구매하기_오늘그만보기', screenShot=screenshot).action(printFail=True)

# action(Clicker('구매하기'), canSkip=True)

# action(Clicker('상점_관심상품'), canSkip=True)
# if action(Clicker('구매하기')):
#     action(Clicker('확인'), canSkip=True)
# action(Clicker('뒤로가기'))
# action(Founder('스케쥴러'))


# robot.pressKey('s', sleep=4)
# imageFinder.findAndClick('구매하기_오늘그만보기', error=False)   
# imageFinder.waitAndClick('상점_관심상품')
# imageFinder.waitAndClick('구매하기', maxWait=3, threshold=0.91, error= False)
# imageFinder.waitAndClick('확인', maxWait=3, threshold=0.91, error=False)
# imageFinder.waitAndClick('확인', maxWait=2, threshold=0.91, error=False)

# find('test2', threshold=0.83)
# find('test')

# action = Clicker('test')
# action.action()
# action = Presser('ESC')
# action.action()






# def find(imageName: str, threshold: float=0.93):
#     global g_prevAction
#     currAction = Clicker(imageName, threshold=threshold)
#     loopCount = 0
#     while True:
#         if loopCount == g_fallbackCount:
#             currAction.action(printFail=True)
#             dun_print.errorf(imageName)
#         if currAction.action() is True:
#             break
#         else:
#             loopCount += 1
#             time.sleep(0.5)
#             if g_prevAction is not None:
#                 g_prevAction.fallback(printOk=False)

#     g_prevAction = currAction

# def press():
#     currAction = Presser('ESC')
#     g_prevAction = currAction
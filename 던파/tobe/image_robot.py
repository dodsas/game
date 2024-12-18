from enum import Enum
import time
import image_finder
import image_clicker
import dun_print
import cv2
import image_keyboard

# g_fallbackCount = 70
g_fallbackCount = 30
g_skipCount = 5
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

    def action(self, printFail=False, printOk=True, screenShot=None, isFallback=False):
        self.fallbackMessage = ''
        if isFallback:
            self.fallbackMessage = 'F_'

        if screenShot is not None:
            self.screenShot = screenShot
        if self.screenShot is None:
            self.screenShot = image_finder.getScreenShotToGray()

        pt, score = image_finder.find(self.imageName, screenShot=self.screenShot, threshold=self.threshold)
        if pt is None:
            if printFail:
                dun_print.printf(self.imageName, f'{self.fallbackMessage}N_FOUND', f'{score:.4f}')
            if self.errorMode:
                dun_print.errorf(self.imageName)
            return False
        else: 
            if printOk:
                dun_print.printf(self.imageName, f'{self.fallbackMessage}FOUND', f'{score:.4f}', f'x:{pt[0]} y:{pt[1]}')
            return True
    
    def fallback(self, screenShot=None):
        # time.sleep(0.1)
        self.action(printFail=True, printOk=True, screenShot=screenShot)

    def name(self):
        return self.imageName

class Clicker(Actionable):
    def __init__(self, imageName: str, threshold: float=0.90, screenShot: cv2.Mat=None, errorMode=False):
        self.imageName = imageName 
        self.threshold = threshold 
        self.screenShot = screenShot
        self.errorMode = errorMode

    def action(self, printFail=False, printOk=True, screenShot=None, isFallback=False):
        self.fallbackMessage = ''
        if isFallback:
            self.fallbackMessage = 'F_'

        if screenShot is not None:
            self.screenShot = screenShot

        pt, score = image_finder.find(self.imageName, screenShot=self.screenShot, threshold=self.threshold)
        if pt is None:
            if printFail:
                dun_print.printf(self.imageName, f'{self.fallbackMessage}N_CLICK', f'{score:.4f}')
            if self.errorMode:
                dun_print.errorf(self.imageName)
            return False
        else: 
            time.sleep(0.5)
            image_clicker.click(pt)
            if printOk:
                dun_print.printf(self.imageName, f'{self.fallbackMessage}CLICK', f'{score:.4f}', f'x:{pt[0]} y:{pt[1]}')
            time.sleep(0.5)
            return True
    
    def fallback(self, screenShot=None):
        # time.sleep(0.3)
        self.action(printFail=True, printOk=True, screenShot=screenShot, isFallback=True)

    def name(self):
        return self.imageName

class Presser(Actionable):
    def __init__(self, key: str, fallbackSkip=False):
        self.key = key 
        self.fallbackSkip = fallbackSkip

    def action(self, printFail=False, printOk=True, screenShot=None):
        if screenShot is not None:
            self.screenShot = screenShot

        image_keyboard.press(self.key, sleep=0, duration=0.01)
        if printOk:
            dun_print.printf('키입력', 'KEY_PRESS', self.key)
        time.sleep(0.1)
        return True

    def fallback(self, screenShot=None):
        time.sleep(0.5)
        if self.fallbackSkip is False:
            self.action(printFail=True, printOk=True, screenShot=screenShot)     

    def name(self):
        return self.key

class Direct(Actionable):
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y 

    def action(self, printFail=False, printOk=True, screenShot=None):
        image_clicker.clickDirect(self.x, self.y)
        if printOk:
            dun_print.printf('클릭', 'DIRECT', str(self.x) + " " + str(self.y))
        return True

    def fallback(self, screenShot=None):
        # time.sleep(0.2)
        self.action(printFail=True, printOk=True, screenShot=screenShot)

    def name(self):
        return str(self.x) + " " + str(self.y)

def do(currAction: Actionable, canSkip=False, onlyOneTime=False, screenShot=None, fallbackSkip=False, okSkip=False):
    global g_prevAction
    global g_fallbackCount
    global g_skipCount

    loopCount = 0
    isOk = False
    # dun_print.printf(currAction.name(), 'START')

    time.sleep(0.5)
    while True:
        if screenShot is None :
            screenShot = image_finder.getScreenShotToGray(currAction.name())
        # skip
        if okSkip is False :
           Clicker('확인', screenShot=screenShot).action(printFail=False)

        if canSkip and loopCount == g_skipCount:
            currAction.action(printFail=True, screenShot=screenShot)
            break
        if loopCount == g_fallbackCount:
            currAction.action(printFail=True, screenShot=screenShot)
            dun_print.errorf(currAction.name())
        if currAction.action(printFail=True, screenShot=screenShot) is True:
            isOk = True
            break
        if onlyOneTime:
            break
        else:
            time.sleep(0.1)
            loopCount += 1
            if g_prevAction is not None and fallbackSkip is False:
                screenShot = image_finder.getScreenShotToGray(currAction.name())
                g_prevAction.fallback(screenShot=screenShot)
            screenShot = None
            # time.sleep(0.5)

    # Clicker('확인', screenShot=screenShot).action(printFail=False)

    if canSkip == False :
        g_prevAction = currAction
    
    # time.sleep(0.2)

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
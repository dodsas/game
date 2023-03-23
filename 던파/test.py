import imageFinder
import robot


test = []
# test.append(imageFinder.findAndClick, ['확인', threshold=0.9, error=False, printLog=True])
test.append((robot.pressKey, ['1']))

for func, args in test:
    result = func(*args)
    print(result)
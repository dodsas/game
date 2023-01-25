import pyautogui
from wcwidth import wcswidth

def pressKey(key: str, sleep: float = 2, duration: float = 1):
    pyautogui.sleep(sleep)
    print('pressKey: ' + key)
    pyautogui.keyDown(key)
    pyautogui.sleep(duration)
    pyautogui.keyUp(key)

def colorFilter(keyword, word, filter, color):
    if keyword in filter:
        return f'\033[{color}m{word}\033[0m'
    else:
        return word 

def lj(str, length):
    retVal = f'{str.ljust(length - (wcswidth(str) - len(str)))}'

    redFilter = [
        'NOT_FOUND',
    ]

    greenFilter = [
        'FOUND',
        '한글',
    ]

    # color code
    # 91: red
    # 92: green
    # 93: yellow
    # 94: blue
    # 95: purple
    # 96: cyan
    # 97: white
    # 98: gray
    # 99: black

    retVal = colorFilter(str, retVal, redFilter, 91)
    retVal = colorFilter(str, retVal, greenFilter, 92)

    return f'[{retVal}]'

# [ 캐릭며어어엉 ]
charName = '캐릭며어어엉'
def printf(p1, p2, p3, p4):
    # print(f'[ {p1.ljust(13-p1Adjust)} ][ {p2:9} ][ {p3:6} ] {p4:15}')
    # print(f'[ {p1.ljust(l(p1, 13))} ][ {p2:9} ][ {p3:6} ] {p4:15}')
    # print(f'{lj(p1, 13)} [ {p2:9} ][ {p3:6} ] {p4:15}')
    print(lj(charName, 12) + lj(p1, 21) + lj(p2, 9) + lj(p3, 6) + lj(p4, 15))

printf('한글', '1', '2', '3')
printf('FOUND', '1', '2', '3')
printf('NOT_FOUND', '1', '2', '3')
charName = '보리앤파이터'
printf('abcd', '1', '2', '3')
charName = '런처꾸꾸'
printf('abcdff', '1', '2', '3')
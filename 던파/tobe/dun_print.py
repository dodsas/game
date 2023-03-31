import pyautogui
import datetime
from wcwidth import wcswidth

import mail_sender

def errorf(imageName: str):
    printf(imageName, 'ERROR')
    # print HH:MM:SS timestamp
    message = f'[{datetime.datetime.now().strftime("%H:%M:%S")}] {imageName} is not found [{g_charName}]'
    mail_sender.sendMail(f'[DNF] IMAGE ERROR', message)
    exit()


def color_filter(keyword, word, filter, color):
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

    retVal = color_filter(str, retVal, redFilter, 91)
    retVal = color_filter(str, retVal, greenFilter, 92)

    return f'[ {retVal} ]'

def printf(p1, p2 = '', p3 = '', p4 = ''):
    print(
        lj(datetime.datetime.now().strftime('%H:%M:%S'), 8) + 
        lj(g_charName, 3) + lj(p1, 21) + lj(p2, 9) + lj(p3, 6) + lj(p4, 15)
    )

g_charName = '캐릭며어어엉'

# errorf("sdafasdf")

# printf('한글', '1', '2', '3')
# printf('FOUND', '1', '2', '3')
# printf('NOT_FOUND', '1', '2', '3')
# charName = '보리앤파이터'
# printf('abcd', '1', '2', '3')
# charName = '런처꾸꾸'
# printf('abcdff', '1', '2', '3')
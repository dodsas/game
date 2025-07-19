from pynput.mouse import Controller
import time

# 마우스 컨트롤러 생성
mouse = Controller()

try:
    while True:
        # 현재 마우스 위치 가져오기
        position = mouse.position
        print(f"현재 마우스 위치: x={position[0]}, y={position[1]}")
        time.sleep(1)  # 1초 대기
except KeyboardInterrupt:
    print("프로그램 종료")
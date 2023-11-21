# import sys
# sys.path.append('tobe')
# from image_robot import * 

# # action(Clicker('상점', threshold=0.78))
# # action(Clicker('상점_상점'))

# # # 자질구리한 팝업 스킵
# # screenshot = image_finder.getScreenShotToGray()
# # Clicker('구매하기_오늘그만보기', screenShot=screenshot).action(printFail=True)

# # action(Clicker('상점_관심상품'), canSkip=True)
# # if action(Clicker('구매하기')):
# #     action(Clicker('확인'))
# #     action(Clicker('확인'), canSkip=True)
# # action(Clicker('뒤로가기'))
# # action(Founder('스케쥴러'))

# do(Founder('산등성이'))
# # action(Direct(1704,446))

# 문자열 "test"를 함수 이름으로 사용하여 함수를 정의합니다.
def test():
    print("Function 'test' has been called!")

# 문자열 "test"를 변수에 저장합니다.
func_name = "test"

# 전역 이름 공간에서 문자열로 된 변수명을 사용하여 함수를 가져옵니다.
function_to_call = globals()[func_name]
globals()[func_name]()

# 가져온 함수를 호출합니다.
function_to_call()
import sys
sys.path.append('tobe')
from image_robot import * 

# action(Clicker('상점', threshold=0.78))
# action(Clicker('상점_상점'))

# # 자질구리한 팝업 스킵
# screenshot = image_finder.getScreenShotToGray()
# Clicker('구매하기_오늘그만보기', screenShot=screenshot).action(printFail=True)

# action(Clicker('상점_관심상품'), canSkip=True)
# if action(Clicker('구매하기')):
#     action(Clicker('확인'))
#     action(Clicker('확인'), canSkip=True)
# action(Clicker('뒤로가기'))
# action(Founder('스케쥴러'))

action(Founder('산등성이'))
# action(Direct(1704,446))
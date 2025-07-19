"""
던파 자동화 - 새로운 이미지 로봇 프레임워크

이 패키지는 던전앤파이터 게임 자동화를 위한 고급 이미지 인식 및 액션 시스템을 제공합니다.
"""

# 핵심 모듈들을 패키지 레벨에서 import
from .image_robot import *
from .image_finder import *
from .image_clicker import *
from .image_keyboard import *
from .dun_print import *
from .mail_sender import *

# 버전 정보
__version__ = "2.0.0"
__author__ = "DnF Automation Team"

# 패키지에서 노출할 주요 클래스/함수들
__all__ = [
    # image_robot 모듈
    'Actionable', 'Clicker', 'Founder', 'Presser', 'Direct', 'do',
    
    # image_finder 모듈  
    'image_finder',
    
    # image_clicker 모듈
    'image_clicker',
    
    # image_keyboard 모듈
    'image_keyboard',
    
    # dun_print 모듈
    'dun_print',
    
    # mail_sender 모듈
    'mail_sender'
]
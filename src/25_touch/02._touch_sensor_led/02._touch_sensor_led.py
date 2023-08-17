# ******************************************************************************************
# FileName     : 02._touch_sensor_led
# Description  : 터치 센서에 터치해서 LED를 켜보기
# Author       : 이승찬
# Created Date : 2021.08.18
# Reference    :
# Modified     : 2022.02.08 : SJI : 헤더 수정, 주석 수정, 소스 크린징
# Modified     : 2023.08.17 : KTW : 코드 수정
# ******************************************************************************************


# import
import time
from machine import Pin
from ETboard.lib.pin_define import *


# global variable
pt = Pin(D6)                    # 터치센서 핀 지정

led_red = Pin(D2)               # 빨강 LED 핀 지정
led_blue = Pin(D3)              # 파랑 LED 핀 지정
led_green = Pin(D4)             # 초록 LED 핀 지정
led_yellow = Pin(D5)            # 노랑 LED 핀 지정




# setup
def setup():
    pt.init(Pin.IN)             # 터치센서 입력모드 설정
    
    led_red.init(Pin.OUT)       # 빨강 LED 출력모드 설정
    led_blue.init(Pin.OUT)      # 파랑 LED 출력모드 설정
    led_green.init(Pin.OUT)     # 초록 LED 출력모드 설정
    led_yellow.init(Pin.OUT)    # 노랑 LED 출력모드 설정
    
    
# main loop
def loop():
    
    
    led_red.value(LOW)          # 빨강 LED 끄기
    led_blue.value(LOW)         # 파랑 LED 끄기
    led_green.value(LOW)        # 초록 LED 끄기
    led_yellow.value(LOW)       # 노랑 LED 끄기
    
    if pt.value() == HIGH:      # 터치시 모든 LED 켜기
        led_red.value(HIGH)     # 빨강 LED 켜기
        led_blue.value(HIGH)    # 파랑 LED 켜기
        led_green.value(HIGH)   # 초록 LED 켜기
        led_yellow.value(HIGH)  # 노랑 LED 켜기
        
    print(pt.value())           # 터치센서 값 출력
    time.sleep(0.1)             # 0.1초 대기
    
    
if __name__ == "__main__":
    setup()
    while True:
        loop()


# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================

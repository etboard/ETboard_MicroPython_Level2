# ******************************************************************************************
# FileName     : 01._dc_motor_sample1
# Description  : DC모터를 이용한 바퀴 전진 해보기
# Author       : 손정인
# Created Date : 2022.02.15
# Reference    :
# Modified     : 2023.08.17 소스코드 수정
# ******************************************************************************************

# import
import time
from machine import Pin
from ETboard.lib.pin_define import *

# global variable
led_red = Pin(D2)                                       # 빨강 LED 핀 지정
led_blue = Pin(D3)                                      # 파랑 LED 핀 지정


# setup
def setup() :
    led_red.init(Pin.OUT)                               # 빨강 LED 출력모드 설정
    led_blue.init(Pin.OUT)                              # 파랑 LED 출력모드 설정
    
# main loop
def loop() :
    
    print("전진")                                       # 전진 출력
    time.sleep(0.5)
    
    led_red.value(HIGH)                                 # 빨강 LED 켜기
    led_blue.value(LOW)                                 # 파랑 LED 끄기
    time.sleep(5)                                       # 5초 기다리기
    
    print("정지")
    led_red.value(LOW)                                  # 빨강 LED 끄기
    led_blue.value(LOW)                                 # 파랑 LED 끄기
    time.sleep(5)                                       # 5초 기다리기
    
if __name__ == "__main__" :
    setup()
    while True :
        loop()
        
# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
# ******************************************************************************************
# FileName     : 01._ultrasonic_sensor
# Description  : 초음파 센서를 이용하여 물체와의 거리 측정 해보기
# Author       : 이승찬
# Created Date : 2021.08.18
# Reference    :
# Modified     : 2022.02.08 : SJI : 헤더 수정, 소스 크린징
# Modified     : 2022.02.15 : SJI : 주석 수정
# Modified     : 2023.08.17 : KTW : 코드 수정
# ******************************************************************************************


# import
import time
from machine import Pin, time_pulse_us
from ETboard.lib.pin_define import *


# global variable
trigPin = Pin(D9)                           # 초음파 송신부
echoPin = Pin(D8)                           # 초음파 수신부


# setup
def setup():
    trigPin.init(Pin.OUT)                   # 초음파 송신부 출력 모드 설정하기
    echoPin.init(Pin.IN)                    # 초음파 수신부 임력 모드 설정하기
    

#main loop
def loop():
    # 초음파 송신 후 수신부는 HIGH 상태로 대기
    trigPin.value(LOW)
    echoPin.value(LOW)
    time.sleep_ms(2)
    trigPin.value(HIGH)
    time.sleep_ms(10)
    trigPin.value(LOW)
    
    
    # echoPin 이 HIGH 를 유지한 시간 저장
    duration = time_pulse_us(echoPin, HIGH)
    # HIGH 였을 때 시간(초음파 송수신 시간)을 기준으로 거리를 계산
    distance = 17 * duration / 1000
    
    # 초음파센서 값을 출력
    print(f'{distance : .2f}', "Cm")                  # 거리를 화면에 출력해줌
    time.sleep(0.5)                                   # 1초 대기
    
    
if __name__ == "__main__":
    setup()
    while True:
        loop()
        
# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================

# ******************************************************************************************
# FileName     : 05._servo_motor_variable_sensor
# Description  : 가변저항으로 서보모터 제어 해보기
# Author       : 이승찬
# Created Date : 2021.08.20
# Reference    :
# Modified     : 2022.02.08 : SJI : 헤더 수정, 소스 크린징
# Modified     : 2023.08.17 : KTW : 코드 수정
# ******************************************************************************************


# import
import time
from machine import Pin
from machine import ADC
from ETboard.lib.pin_define import *
from ETboard.lib.servo import Servo


# global variable
servo = Servo(Pin(D6))                          # 서보모터 핀 지정
sensor = ADC(Pin(A0))                           # 가변저항 핀 지정


# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)


# mainloop
def loop():
    servo.write_angle(int(sensor.read()/15))    # 가변저항 값을 서보모터 값으로 설정
    
    sensor_result = sensor.read()               # 가변저항 센서 값 저장
    print(sensor_result)                        # 가변저항 센서 값 출력
    
    time.sleep(0.1)                             # 0.1초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()
# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================

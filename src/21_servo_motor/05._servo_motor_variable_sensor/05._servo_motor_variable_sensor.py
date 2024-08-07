# ******************************************************************************************
# FileName     : 05._servo_motor_variable_sensor
# Description  : 가변저항으로 서보모터 제어 해보기
# Author       : 이승찬
# Created Date : 2021.08.20
# Reference    :
# Modified     : 2022.02.08 : SJI : 헤더 수정, 소스 크린징
# ******************************************************************************************


# import
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


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================

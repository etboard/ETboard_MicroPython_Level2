# ******************************************************************************************
# FileName     : ultrasonic_servo_motor
# Description  : 초음파 센서의 거리에 따라 서보모터를 제어 해보기
# Author       : 이승찬
# Created Date : 2021.08.20
# Reference    :
# Modified     : 2022.02.08 : SJI : 헤더 수정, 주석 수정
# Modified     : 2023.08.17 : KTW : 코드 수정 
# ******************************************************************************************

# import
import time
from machine import Pin, time_pulse_us
from ETboard.lib.pin_define import *
from ETboard.lib.servo import Servo


# global variable
servo = Servo(Pin(D2))                                   # 서보모터 핀 지정
trigPin = Pin(D9)                                        # 초음파 송신부 핀 지정
echoPin = Pin(D8)                                        # 초음파 수신부 핀 지정



# set up
def setup():
    trigPin.init(Pin.OUT)                                # 초음파 송신부 출력모드 설정
    echoPin.init(Pin.IN)                                 # 초음파 수신부 입력모드 설정
    
    
# main loop
def loop():
    trigPin.value(LOW)
    echoPin.value(LOW)
    time.sleep_ms(2)
    trigPin.value(HIGH)
    time.sleep_ms(10)
    trigPin.value(LOW)
    
    duration = time_pulse_us(echoPin, HIGH)
    distance = 17 * duration / 1000
    
    
    if distance < 20:                                    # 물체와의 거리가 20cm 미만이면 180도로 설정
        servo.write_angle(180)
        
    if distance >= 20:                                   # 물체와의 거리가 20cm 이상이면 0도로 설정
        servo.write_angle(0)
        
    print(f'{distance : .2f}', "Cm")                     # 거리를 화면에 출력해줌
    time.sleep(0.5)                                      # 0.5초 대기
    
if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================

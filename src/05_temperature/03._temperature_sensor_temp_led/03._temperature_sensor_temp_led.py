# ******************************************************************************************
# FileName     : 03._temperature_sensor_temp_led
# Description  : 온도 센서 값을 을 이용해 LED 켜보기
# Author       : 이승찬
# Created Date : 2021.08.17
# Reference    :
# Modified     : 2022.02.08 : SJI : 헤더 수정, 주석 수정, 소스 크린징
# Modified     : 2023.08.17 : KTW : 코드 수정
# ******************************************************************************************


# import
import time
import math
from machine import ADC, Pin
from ETboard.lib.pin_define import *


#global variable
R1 = 10000
c1 = 1.009249522e-03
c2 = 2.378405444e-04
c3 = 2.019202697e-07

sensor = ADC(Pin(A2))                                     # 온도센서 핀 지정

led_red = Pin(D2)                                         # 빨강 LED 핀 지정
led_blue = Pin(D3)                                        # 파랑 LED 핀 지정
led_green = Pin(D4)                                       # 초록 LED 핀 지정
led_yellow = Pin(D5)                                      # 노랑 LED 핀 지정



# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)                           # 온도센서 입력모드 설정

    led_red.init(Pin.OUT)                                 # 빨간 LED 출력모드 설정
    led_blue.init(Pin.OUT)                                # 파란 LED 출력모드 설정
    led_green.init(Pin.OUT)                               # 초록 LED 출력모드 설정
    led_yellow.init(Pin.OUT)                              # 노랑 LED 출력모드 설정


#main loop
def loop():
    Vo = sensor.read()                                    # 가변저항 센서 값 저장
    sensor_result = sensor.read()                         # 온도센서 값 저장

    R2 = R1 * (4095.0 / Vo - 1.0)                         # 온도 센서 값을 이용하여 실제 온도 값 으로 변환
    logR2 = math.log(R2)
    T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2))
    Tc = T - 273.15

    if Tc < 25:                                           # 온도가 25도 미만이면 파랑 LED 켜기
        led_red.value(LOW)
        led_blue.value(HIGH)
        led_green.value(LOW)
        led_yellow.value(LOW)
        print("파랑온")

    if Tc >= 25 and Tc < 27:                              # 온도가 25도 이상 27도 미만이면 초록 LED 켜기
        led_red.value(LOW)
        led_blue.value(LOW)
        led_green.value(HIGH)
        led_yellow.value(LOW)
        print("초록온")
  
    if Tc >= 27 and Tc < 29:                              # 온도가 27도이상 29도 미만이면 노랑 LED 켜기
        led_red.value(LOW)
        led_blue.value(LOW)
        led_green.value(LOW)
        led_yellow.value(HIGH)
        print("노랑온")

    if Tc >= 29:                                          # 온도가 29도 이상이면 빨강 LED 켜기
        led_red.value(HIGH)
        led_blue.value(LOW)
        led_green.value(LOW)
        led_yellow.value(LOW)
        print("빨강온")

    print(f'{Tc:0.2f}', "°C")                             # 온도 변환 값 출력
    time.sleep(0.2)                                       # 0.2초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()


# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================

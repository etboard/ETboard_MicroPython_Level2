# ******************************************************************************************
# FileName     : 01._dht11
# Description  : 온습도(DHT11) 센서 값 출력 해보기
# Author       : 손철수
# Created Date : 2023.07.28
# Reference    :
# Modified     : 2023.08.17 KTW 소스코드 수정
# ******************************************************************************************


# import
import time
from machine import Pin
from ETboard.lib.pin_define import *
import dht

# global variable
sensor = dht.DHT11(Pin(D2))                             # 온습도(DHT11) 센서 핀 지정

# setup
def setup():
    pass                                                # 아무것도 안함


# main loop
def loop():
    sensor.measure()                                    # 온습도 센서 값 측정
    print(str(sensor.temperature()) + 'C',              # 온도 값 출력
          str(sensor.humidity()) + '%')                 # 습도 값 출력
     
    time.sleep(1)                                       # 1초 기다리기
    
    
    
if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================


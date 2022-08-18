# ******************************************************************************************
# FileName     : buzzer_oled
# Description  : 부저를 이용하여 멜로디를 내고 
#                OLED 모듈에 현재 멜로디를 표시(mario)
# Author       : 이승찬
# Created Date : 2022.08.18
# Reference    :
# Modified     : 
# ******************************************************************************************

# import
import machine
import time
from machine import Pin
from ETboard.lib.pin_define import *
from ETboard.lib.pitches import *
from ETboard.lib.OLED_U8G2 import *

# global variable
buzzer_pin = machine.Pin(D6, machine.Pin.OUT)
buzzer = machine.PWM(buzzer_pin)
oled = oled_u8g2()


melody_notes = [ NOTE_E7, NOTE_E7, 0, NOTE_E7, 0, NOTE_C7, NOTE_E7, 0, NOTE_G7, 0, 0, 0, NOTE_G6, 0, 0, 0, NOTE_C7, 0, 0, NOTE_G6, 0, 0, NOTE_E6, 0, 0, NOTE_A6, 0, NOTE_B6, 0, NOTE_AS6, NOTE_A6, 0, NOTE_G6, NOTE_E7, NOTE_G7, NOTE_A7, 0, NOTE_F7, NOTE_G7, 0, NOTE_E7, 0, NOTE_C7, NOTE_D7, NOTE_B6, 0, 0, NOTE_C7, 0, 0, NOTE_G6, 0, 0, NOTE_E6, 0, 0, NOTE_A6, 0, NOTE_B6, 0, NOTE_AS6, NOTE_A6, 0, NOTE_G6, NOTE_E7, NOTE_G7, NOTE_A7, 0, NOTE_F7, NOTE_G7, 0, NOTE_E7, 0, NOTE_C7, NOTE_D7, NOTE_B6, 0, 0 ]
noteDurations = [ 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 9, 9, 9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 9, 9, 9, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, ]

volume = 1
melody_num = 0
oled.clear()
 
oled.setLine(2, "Mario")          # Mario 출력
oled.display()                    # OLED에 표시

for melody in melody_notes:
    time_length = noteDurations[ melody_num ] / 100
    
    print(f'{melody_num:3}, {melody:5}, {time_length:6.2}')
    melody_num = melody_num + 1

    buzzer.freq(melody)           # 부저의 피치(음 높낮이)
    buzzer.duty(volume)           # 부저의 볼륨
    time.sleep(time_length)       # 소리를 내는 시간
    buzzer.duty(0)                # 초기화

buzzer.deinit()                   # 버저 자체를 초기화    
 
# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================

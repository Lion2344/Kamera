import board
import busio
import digitalio
import adafruit_requests as requests
import wifi
import time
import os

def Test():
    for i in range(2):
        sdcard.ReadWriteToSD(
        entry= time.struct_time(time.localtime()),
        method='a',
        file_name='test.txt'
        )
        sdcard.ReadWriteToSD(
        method='r',
        file_name='test.txt'
        )
        time.sleep(5)
        
    lights.ToggleLight(name_of_light='Green', duration=5)
#Test()



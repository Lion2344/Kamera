from machine import Pin, Timer
import time

def InitLEDs():
    led_ar = [
        Pin('LED', Pin.OUT), #Board
        Pin(13, Pin.OUT),	#Red
        Pin(14, Pin.OUT),	#Yellow
        Pin(15, Pin.OUT)	#Green
        ]   
    return led_ar

def ToggleBoard():
    Pin('LED', Pin.OUT).toggle()
    
def ToggleRed():
    Pin(13, Pin.OUT).toggle()
    
def ToggleYellow():
    Pin(14, Pin.OUT).toggle()
    
def ToggleGreen():
    Pin(15, Pin.OUT).toggle()
    
def KillTheLights():
    for led in InitLEDs():
        led(0)

def LedSetup():
    def blink(timer):
        ledRed.toggle()
        time.sleep(0.1)
        ledYellow.toggle()
        time.sleep(0.1)
        ledGreen.toggle()
        time.sleep(0.1)
        ledPico.toggle()
        time.sleep(1)
    ledPico = Pin('LED', Pin.OUT)
    ledRed = Pin(13, Pin.OUT)
    
    ledYellow = Pin(14, Pin.OUT)
    ledGreen = Pin(15, Pin.OUT)
     
    timer = Timer()
    timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
    

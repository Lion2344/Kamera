import time
import board
from digitalio import DigitalInOut, Direction, Pull

def ToggleLight(name_of_light:str, duration: int=1):
    
    dict_lights = {
        'OnBoard': board.LED,
        'Red': board.GP13,
        'Yellow': board.GP14,
        'Green': board.GP15
    }
    
    led = DigitalInOut(dict_lights[name_of_light])
    led.direction = Direction.OUTPUT
    
    led.value = True
    time.sleep(duration)
    led.value = False
    led.deinit()
    





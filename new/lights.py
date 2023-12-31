import time
import board
from digitalio import DigitalInOut, Direction

def DictLights():
    dict_lights = {
        'OnBoard': board.LED,
        'Red': board.GP13,
        'Yellow': board.GP14,
        'Green': board.GP15,
        'White': board.GP16
    }
    return dict_lights

def ToggleLight(name_of_light: str, duration: int=1):
    dict_lights = DictLights()
    
    led = DigitalInOut(dict_lights[name_of_light])
    led.direction = Direction.OUTPUT
    
    if name_of_light == 'White':
        time.sleep(duration)
        
>>>>>>> Test
    led.value = True
    time.sleep(duration)
    led.value = False
    led.deinit()
    
def GetLight(name_of_light: str()):
    
    pin = DictLights()[name_of_light]
    try:
        # Try to initialize the pin; if it's already in use, an exception will be raised.
        pin_obj = DigitalInOut(pin)
        pin_obj.direction = Direction.OUTPUT
        return pin_obj
    except ValueError:
        # The pin is already in use, so release it and reassign it for the new use.
        pin_obj = DigitalInOut(pin)
        pin_obj.deinit()
        pin_obj = DigitalInOut(pin)
        pin_obj.direction = Direction.OUTPUT
        return pin_obj

def Error():
    for led in DictLights():
        ToggleLight(name_of_light=led, duration=0.3)

# Define your pin assignments and their new uses.
#pin_to_check = "Yellow"
#new_direction = Direction.OUTPUT
#new_use = "Yellow"

# Check and assign the pin.
#assigned_pin = check_and_assign_pin(name_of_light='Yellow', value=True)

# Perform your operations with the assigned pin.
#assigned_pin.value = True
#time.sleep(2)
#assigned_pin.value = False
#assigned_pin.deinit()




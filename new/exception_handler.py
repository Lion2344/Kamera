#https://learn.adafruit.com/adafruit-micro-sd-breakout-board-card-tutorial/circuitpython
import sdcard


def PrintError(function_name, error):
    
    ReadWriteToSD(file_name="error.txt", entry=f"error in {function_name}: error")
    #print(f'An exception occured in {function_name}: {error}')

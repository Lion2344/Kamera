#https://learn.adafruit.com/adafruit-micro-sd-breakout-board-card-tutorial/circuitpython

def PrintError(error: ValueError, function_name: str=''):
    print(f'An exception occured in {function_name}: {error}')

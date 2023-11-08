#https://learn.adafruit.com/adafruit-micro-sd-breakout-board-card-tutorial/circuitpython
import exception_handler

import os
import board
import busio
import sdcardio
import storage
import lights
import time

def InitialiseSD():
    try:
        spi = busio.SPI(board.GP10, MOSI=board.GP11, MISO=board.GP12)
        cs = board.GP17

        sdcard = sdcardio.SDCard(spi, cs)
        vfs = storage.VfsFat(sdcard)
        storage.mount(vfs, "/sd")
    except Exception as error:
        print(error)
    
def ReadWriteToSD(file_name: str, entry: str='', path: str='', method: str='w'):
    """
    method can be:
        w (over)write file
        wb write binary data 
        a append existing file
        r read file
    """
    print('initialise SD...')
    InitialiseSD()
    print('done')
    
    if path =='':
        path = f"/sd/{file_name}"
    else:
        path = f"/sd/{path}/{file_name}"
    
    print('open file')
    try:
        file = open(path, method)
    except Exception as error:
        print(error)
        
    print('writing on sdcard...')
    time.sleep(0.2)
    lights.ToggleLight('White', duration=0.5)
    try:
        file.write(entry)
    except:
        lights.ToggleLight('White', duration=5)
        print(error)
    
    time.sleep(0.2)
    lights.ToggleLight('White', duration=0.5)
    print('done')
    file.close()
    time.sleep(0.2)
    lights.ToggleLight('White', duration=0.5)
    print('file closed')
    """
    with open(path, method) as f:
        if method == 'w':
            f.write(str(entry))
        elif method == 'a':
            f.write(f'\n{str(entry)}')
        elif method == 'wb':    
            print('writting on sdcard...')
            f.write(arrays)
            print('done')
        elif method == 'r':
            line = f.readline()
            while line != '':
                print(line)
                line = f.readline()
    """ 


def PrintDirectory(path, tabs=0):
    InitialiseSD()
    for file in os.listdir(path):
        stats = os.stat(path + "/" + file)
        filesize = stats[6]
        isdir = stats[0] & 0x4000

        if filesize < 1000:
            sizestr = str(filesize) + " by"
        elif filesize < 1000000:
            sizestr = "%0.1f KB" % (filesize / 1000)
        else:
            sizestr = "%0.1f MB" % (filesize / 1000000)

        prettyprintname = ""
        for _ in range(tabs):
            prettyprintname += "   "
        prettyprintname += file
        if isdir:
            prettyprintname += "/"
        print('{0:<40} Size: {1:>10}'.format(prettyprintname, sizestr))

        # recursively print directory contents
        if isdir:
            PrintDirectory(path + "/" + file, tabs + 1)

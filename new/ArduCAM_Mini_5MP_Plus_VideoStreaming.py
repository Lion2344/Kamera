import sdcard
import lights
import exception_handler

import time
import busio
import board
from Arducam import *
from board import *

def StartCamera():

    mycam.Camera_Init()
    mycam.Spi_write(ARDUCHIP_TIM,VSYNC_LEVEL_MASK)

    mycam.clear_fifo_flag()
    mycam.Spi_write(ARDUCHIP_FRAMES,0x00)
    mycam.set_format(JPEG)
    mycam.OV5642_set_JPEG_size(OV5642_320x240);

    return mycam

def read_fifo_burst(filename: str(), mycam, once_number=128):
    count=0
    lenght=mycam.read_fifo_length()
    mycam.SPI_CS_LOW()
    mycam.set_fifo_burst()
<<<<<<< HEAD

    buffer = bytearray(once_number)
    _buffer = bytearray(once_number)
=======
    buffer=bytearray(once_number)
    _buffer = bytearray()
>>>>>>> Test
    while True:
        mycam.spi.readinto(buffer,start=0,end=once_number)
        _buffer += buffer
        count+=once_number
        if count+once_number>lenght:
            count=lenght-count
            mycam.spi.readinto(buffer,start=0,end=count)
            _buffer+=buffer
            print('call sd...')
            sdcard.ReadWriteToSD(file_name=f'{filename}.jpg', entry=_buffer, method='wb')
            mycam.SPI_CS_HIGH()
            mycam.clear_fifo_flag()
            
            break

    return mycam

def TakePicture(filename: str(), mycam):
    #parameters = Parameters()
    #mycam.OV5642_set_JPEG_size(parameters['sizes'][0])
    #mycam.OV5642_set_Light_Mode(parameters['light_modes'][0])
    #mycam.OV5642_set_Color_Saturation(parameters['color_saturations'][0])
    #mycam.OV5642_set_Brightness(parameters['brightnesses'][0])    
    #mycam.OV5642_set_Contrast(parameters['contrasts'][0])
    #mycam.OV5642_set_hue(parameters['hues'][0])   
    #mycam.OV5642_set_Special_effects(parameters['special_effects'][0])
    #mycam.OV5642_set_Exposure_level(parameters['exposure_levels'][0])
    #mycam.OV5642_set_Sharpness(parameters['sharpnesses'][0]) 
    #mycam.OV5642_set_Mirror_Flip(parameters['mirror_flips'][0])
    #mycam.OV5642_set_Compress_quality(parameters['compress_qualities'][0])
    #mycam.OV5642_Test_Pattern(parameters['test_patterns'][0])

    mycam.flush_fifo();
    mycam.clear_fifo_flag();
    print('start capture')
    mycam.start_capture();


    print('read burst...')
    read_fifo_burst(filename=filename, mycam=mycam)
    print('done')
    print('clear the capture...')
    mycam.clear_fifo_flag()
    print('done')
    
    return mycam

<<<<<<< HEAD
lights.ToggleLight('Green')
lights.ToggleLight('White')
then = time.time()
=======
>>>>>>> Test
led_yellow = lights.GetLight(name_of_light='Yellow')
led_green = lights.GetLight(name_of_light='Green')
led_red = lights.GetLight(name_of_light='Red')

nbr = 3
        
    except:
        led_red.value = True
        led_yellow.deinit()
        led_green.deinit()
        break    
    
    time.sleep(1)

led_yellow.deinit()
led_green.deinit()




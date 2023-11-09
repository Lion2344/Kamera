import sdcard
import lights
import exception_handler

import time
import busio
import board
from Arducam import *
from board import *

<<<<<<< HEAD

def StartCam():
    #stop_flag=0
    #value_command=0
    #flag_command=0

    mycam = ArducamClass(OV5642)
    mycam.Camera_Detection()
    mycam.Spi_Test()

    mycam.Camera_Init()
    mycam.Spi_write(ARDUCHIP_TIM,VSYNC_LEVEL_MASK)
    mycam.clear_fifo_flag()
    mycam.Spi_write(ARDUCHIP_FRAMES,0x00)
    mycam.set_format(JPEG)
    mycam.OV5642_set_JPEG_size(OV5642_320x240);
    mycam.start_capture();
    
    return mycam

def read_fifo_burst(filename: str(), once_number: int=128):
=======
stop_flag=0
once_number=128
value_command=0
flag_command=0

mycam = ArducamClass(OV5642)
mycam.Camera_Detection()
mycam.Spi_Test()

mycam.Camera_Init()
mycam.Spi_write(ARDUCHIP_TIM,VSYNC_LEVEL_MASK)
#utime.sleep(1)
mycam.clear_fifo_flag()
mycam.Spi_write(ARDUCHIP_FRAMES,0x00)
mycam.set_format(JPEG)
mycam.OV5642_set_JPEG_size(OV5642_320x240);
mycam.start_capture();

def read_fifo_burst(filename: str()):

>>>>>>> Test
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

def TakePicture(filename: str()):
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
    read_fifo_burst(filename=filename)
    print('done')
    print('clear the capture...')
    mycam.clear_fifo_flag()
    print('done')

<<<<<<< HEAD
lights.ToggleLight('Green')
lights.ToggleLight('White')
then = time.time()
=======
>>>>>>> Test
led_yellow = lights.GetLight(name_of_light='Yellow')
led_green = lights.GetLight(name_of_light='Green')
led_red = lights.GetLight(name_of_light='Red')

<<<<<<< HEAD

mycam = StartCam()
lights.ToggleLight('White')

for i in range(3):
    print(f"{i}/2")
    led_yellow.value = True
    led_green.value = False
    led_red.value = False
    try:
        TakePicture(filename=i)
        lights.ToggleLight('White')
        led_green.value = True
        led_yellow.value = False
    except:
        led_red.value = True
        led_yellow.deinit()
        led_green.deinit()
        #lights.Error()
        break
    time.sleep(1)

duration = time.time() - then
=======
nbr = 99
gap = 0
zu_lang = True
while zu_lang == True:
    zu_lang = False
    gap += 0.1
    how_often = 0
    for i in range(nbr):
        time_beginning = time.time()
        print(f"{i}/{nbr}")
        led_yellow.value = True
        led_green.value = False
        led_red.value = False
        try:
            TakePicture(filename=i)
            
            duration = time.time() - time_beginning     
            led_green.value = True
            left = gap - duration
            
            if left > 0:
                time.sleep(left)
            else:
                zu_lang = True
                how_often += 1
            led_yellow.value = False
            
        except:
            led_red.value = True
            led_yellow.deinit()
            led_green.deinit()
            #lights.Error()
            break
        
    if zu_lang == True:
        _string = f'duration:{duration}, Left:{left}'
        _string = f' Gap={gap} > Duration: {how_often} times'
        sdcard.WriteDurration(_string)
    


>>>>>>> Test
led_yellow.deinit()
led_green.deinit()




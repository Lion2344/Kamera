import sdcard
import lights

import time
import busio
import board
import usb_cdc
from Arducam import *
from board import *


stop_flag=0
once_number=128
value_command=0
flag_command=0
buffer=bytearray(once_number)
#for b in buffer:
#    print(b)
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
    count=0
    lenght=mycam.read_fifo_length()
    mycam.SPI_CS_LOW()
    mycam.set_fifo_burst()
    _buffer = bytearray()
    while True:
        mycam.spi.readinto(buffer,start=0,end=once_number)
        _buffer += buffer
        count+=once_number
        if count+once_number>lenght:
            count=lenght-count
            mycam.spi.readinto(buffer,start=0,end=count)
            _buffer+=buffer
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


    print('ACK CMD CAM Capture Done.')
    print(read_fifo_burst(filename=filename))
    print('Clear the capture done flag')
    mycam.clear_fifo_flag()
    print('Cleared')

then = time.time()
led_yellow = lights.GetLight(name_of_light='Yellow')
led_green = lights.GetLight(name_of_light='Green')

for i in range(3):
    led_yellow.value = True
    led_green.value = False
    TakePicture(filename=i)
    led_yellow.value = False
    led_green.value = True
    time.sleep(3)

duration = time.time() - then
led_yellow.deinit()
led_green.deinit()
print(duration)



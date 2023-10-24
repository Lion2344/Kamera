import time as utime
import busio
import board
import usb_cdc
from Arducam import *
from board import *

mode = 0
start_capture = 0
stop_flag=0
once_number=128
value_command=0
flag_command=0
buffer=bytearray(once_number)
mycam = ArducamClass(OV5642)
mycam.Camera_Detection()
mycam.Spi_Test()
mycam.Camera_Init()
mycam.Spi_write(ARDUCHIP_TIM,VSYNC_LEVEL_MASK)
utime.sleep(1)
mycam.clear_fifo_flag()
mycam.Spi_write(ARDUCHIP_FRAMES,0x00)

import board
import busio
import displayio
#import adafruit_ssd1306  # Change this import to match your display
import time
#import adafruit_ov5640  # Make sure you have the required library for your camera module
from OV2640_reg import *
from OV5642_reg import *

# Initialize I2C bus for your display
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the OLED display (change the display driver accordingly)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Initialize the camera (change the pins and resolution according to your camera)
camera = adafruit_ov5640.OV5640(
    i2c,
    mclk=board.D9,
    href=board.D10,
    reset=board.D11,
    cs=board.D12,
    password=0x78,
    size=adafruit_ov5640.OV5640_SIZE_QVGA,
)

# Create a display group for the image
display_group = displayio.Group()

# Capture an image
camera.capture_to_disk("/image.bmp")

# Load the captured image and display it on the screen
image_file = open("/image.bmp", "rb")
image = displayio.OnDiskBitmap(image_file)
image_sprite = displayio.TileGrid(image, pixel_shader=displayio.ColorConverter())
display_group.append(image_sprite)
display.show(display_group)

# Delay for a few seconds to view the image (you can adjust this as needed)
time.sleep(5)

# Clean up
image_file.close()
camera.deinit()
display.fill(0)
display.show()

# Optionally, you can delete the captured image file
import os
os.remove("/image.bmp")

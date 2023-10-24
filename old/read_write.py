import machine
import sdcard
import uos
import lights
import time
    
def SDTest():
    lights.ToggleYellow()
    CS = machine.Pin(17, machine.Pin.OUT)
    spi = machine.SPI(
        1,
        baudrate=1000000,
        polarity=0,
        phase=0,
        bits=8,
        firstbit=machine.SPI.MSB,
        sck=machine.Pin(10),
        mosi=machine.Pin(11),
        miso=machine.Pin(12))

    sd = sdcard.SDCard(spi,CS)

    vfs = uos.VfsFat(sd)
    uos.mount(vfs, "/sd")

    # Create a file and write something to it
    with open("/sd/data.txt", "w") as file:
        print("Writing to data.txt...")
        file.write("Welcome to microcontrollerslab134!\r\n")
        file.write("This is a test\r\n")

    # Open the file we just created and read from it
    with open("/sd/data.txt", "r") as file:
        print("Reading data.txt...")
        data = file.read()
        print(data)

    lights.ToggleGreen()
    time.sleep(2)
    lights.KillTheLights()

def WriteSDCard(file):
    lights.ToggleYellow()
    CS = machine.Pin(17, machine.Pin.OUT)
    spi = machine.SPI(
        1,
        baudrate=1000000,
        polarity=0,
        phase=0,
        bits=8,
        firstbit=machine.SPI.MSB,
        sck=machine.Pin(10),
        mosi=machine.Pin(11),
        miso=machine.Pin(12))

    sd = sdcard.SDCard(spi,CS)

    vfs = uos.VfsFat(sd)
    uos.mount(vfs, "/sd")
    
    try:
        with open(f"/sd/{file}.jpg", "w") as file:
            print("Writing to data.txt...")
            file.write(file)
        lights.ToggleGreen()
   
    except:
        lights.ToggleRed()
        
    time.sleep(2)
    lights.KillTheLights()
import lights
import sdcard
import internet


import usb_cdc

usb_cdc.enable(data=True)
sdcard.InitialiseSD()

for i in range(3):
    for l in ['OnBoard', 'Red', 'Yellow', 'Green']:
        lights.ToggleLight(name_of_light=l, duration=0.1)

#internet.ConnectToWifi()

#import ArduCAM_Mini_5MP_Plus_VideoStreaming
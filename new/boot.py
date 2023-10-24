import lights
import sdcard
import internet
import main

import usb_cdc

usb_cdc.enable(data=True)
sdcard.InitialiseSD()

for i in range(3):
    for l in ['OnBoard', 'Red', 'Yellow', 'Green']:
        lights.ToggleLight(name_of_light=l, duration=0.1)

internet.ConnectToWifi()

try:
    lights.ToggleLight('Yellow', 5)
    main.Test()
except:
    lights.ToggleLight('Red', 5)
lights.ToggleLight('Green', 2)
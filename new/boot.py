import lights
import sdcard
import internet

import usb_cdc

usb_cdc.enable(data=True)
sdcard.InitialiseSD()

for l in ['OnBoard', 'Red', 'Yellow', 'Green']:
    lights.ToggleLight(l)

internet.ConnectToWifi()
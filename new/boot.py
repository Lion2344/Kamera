import lights
import sdcard

import usb_cdc

usb_cdc.enable(data=True)
sdcard.InitialiseSD()

for l in ['OnBoard', 'Red', 'Yellow', 'Green', 'OnBoard']:
    lights.ToggleLight(l)


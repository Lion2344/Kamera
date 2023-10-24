import usb_cdc
usb_cdc.enable(data=True)

import lights


for l in ['OnBoard', 'Red', 'Yellow', 'Green']:
    lights.ToggleLight(l)

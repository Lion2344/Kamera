import lights

for i in range(3):
    for l in ['OnBoard', 'Red', 'Yellow', 'Green']:
        lights.ToggleLight(name_of_light=l, duration=0.1)
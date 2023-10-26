import lights

import time
import ipaddress
import wifi
import os

def ConnectToWifi():
    leds = [
        lights.GetLight(name_of_light='Red'),
        lights.GetLight(name_of_light='Yellow'),
        lights.GetLight(name_of_light='Green')
    ]
    
    leds[1].value = True
    try:
        wifi.radio.connect(os.getenv("WIFI_SSID"), os.getenv("WIFI_PASSWORD"))
        leds[2].value = True
    except:
        leds[0].value = True
    
    time.sleep(1)
    for led in leds:
        led.deinit()

    
def ScanningAvailableNetwork():
    networks = wifi.radio.start_scanning_networks()
    for network in networks:
        print("SSID:", network.ssid)
        
def TestConnection():
    # Check Wi-Fi connection status
    ping_ip = ipaddress.IPv4Address("8.8.8.8")
    ping = wifi.radio.ping(ip=ping_ip) * 1000
    if ping is not None:
        print(f"Ping google.com: {ping} ms")
    else:
        ping = wifi.radio.ping(ip=ping_ip)
        print(f"Ping google.com: {ping} ms")


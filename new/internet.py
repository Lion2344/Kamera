import lights

import ipaddress
import wifi
import os

def ConnectToWifi():    
    lights.ToggleLight(name_of_light='Yellow')
    try:
        wifi.radio.connect(os.getenv("WIFI_SSID"), os.getenv("WIFI_PASSWORD"))
        lights.ToggleLight(name_of_light='Green')
    except:
        lights.ToggleLight(name_of_light='Red')
    wifi.radio.disconnect()

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


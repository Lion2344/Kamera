import network
import lights
import time


def ScanWifiNetwork():
    wlan = network.WLAN(network.STA_IF) #  network.WLAN(network.STA_IF)
    wlan.active(True)
    networks = wlan.scan()
    print(networks)
    
def ConnectToWifi(ssid=b'Simon\xe2\x80\x99s iPhone', password='12345678'):
    lights.InitLEDs()[0](1)

    #Ländereinstellung
    network.country('DE')

    #Client-Betrieb
    wlan = network.WLAN(network.STA_IF)

    #WLAN-Interface aktivieren
    wlan.active(True)

    #WLAN-Verbindung herstellen
    wlan.connect(ssid, password)

    #WLAN-Verbindungsstatus prüfen
    
    print('Warten auf WLAN-Verbindung')

    while not wlan.isconnected() and wlan.status() >= 0:
        lights.InitLEDs()[1](1)
        lights.ToggleYellow()
        time.sleep(0.5)
    
    if wlan.status() == -2:
        print("WiFi not found")
        lights.KillTheLights()
        lights.InitLEDs()[1](1)
        
        return None
    else:
        print('WLAN-Verbindung hergestellt / Status:', wlan.status())
        lights.InitLEDs()[1](0)
        lights.InitLEDs()[2](0)
        lights.InitLEDs()[3](1)
    
        ip = wlan.ifconfig()[0]
        print(f'Connected on {ip}')
    
        time.sleep(2)
        lights.KillTheLights()

        return ip 
    
def DisconnectFromWlan():
    wlan = network.WLAN(network.STA_IF)
    wlan.disconnect()
    print('WLAN-Verbindung gekappt / Status:', wlan.status())

import socket
def open_socket(ip, port=80):
    # Open a socket
    address = (ip, port)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

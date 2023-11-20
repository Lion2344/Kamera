import lights
import internet
import time 
import os, ssl, socketpool, wifi
import adafruit_minimqtt.adafruit_minimqtt as MQTT
from microcontroller import cpu

internet.ConnectToWifi()

#Create a socket pool
pool = socketpool.SocketPool(wifi.radio)

#Get adafruit io username and key from settings.toml
aio_username = os.getenv('AIO_USERNAME')
aio_key = os.getenv('AIO_KEY')

#Setup a feed: This may have a different name tha you Dashboard
strip_on_off_feed = aio_username + "/feeds/strip_on_off"
temperature_feed = aio_username + "/feeds/temperature"
pic_feed = aio_username + "/feeds/pic"

#Setup functions to respond to MQTT events
def subscribe(client, userdata, topic, granted_qos):
    # This method is called when the client subscribes to a new feed.
    print("Subscribed to {0} with QOS level {1}".format(topic, granted_qos))
    
def connected(client, userdata, flags, rc):
    # Connected to broke at adafruit io
    print("Connected to Adafruit IO! Listening for topic changes I have subscribed to")
    #Subscribe to all changes on the feed
    client.subscribe(strip_on_off_feed)
    client.subscribe(temperature_feed)
    client.subscribe(pic_feed)
    
def disconnected(client, userdata, rc):
    #Disconnected from the broker at adafruit IO!
    print("Disconnected from Adafruit IO!")
    
def message(client, topic, message):
    #The bulk of your code to respond to MQTT will be here
    print(f"topic: {topic}, message: {message}")
    if message == "ON":
        lights.ToggleLight('Green')
    elif message == "OFF":
        lights.ToggleLight('Red')
        
mqtt_client = MQTT.MQTT(
    broker=os.getenv("BROKER"),
    port=os.getenv("PORT"),
    username=aio_username,
    password=aio_key,
    socket_pool=pool,
    ssl_context=ssl.create_default_context(),
)

mqtt_client.on_connect = connected
mqtt_client.on_disconnect = disconnected
mqtt_client.on_message = message
mqtt_client.on_subscribe = subscribe

print("Connecting to Adafruit IO...")
mqtt_client.connect()
lights.ToggleLight('White')
j = 0
i = 10

import ArduCAM_Mini_5MP_Plus_VideoStreaming as aducam

mycam = aducam.StartCamera()
mycam, buffer = aducam.TakePicture(filename='Test', mycam=mycam)
_buffer = buffer[:128]
while j <= i:
    #keep checking the mqtt message queue
    mqtt_client.loop()
    #If you had other non mqtt code, you coul add it here
    # Send a new temperature reading to IO every 30 seconds

    # take the cpu's temperature
    cpu_temp = cpu.temperature
    # truncate to two decimal points
    cpu_temp = str(cpu_temp)[:5]
    #print("CPU temperature is %s degrees C" % cpu_temp)
    # publish it to io
    #print("Publishing %s to temperature feed..." % cpu_temp)
    start = 0
    mqtt_client.publish(pic_feed, '##########################################')
    for _b in range(0, len(buffer), 128):
        end = _b
        print(f'start: {start} end: {end}')
        _buffer = buffer[start:end]
        mqtt_client.publish(pic_feed, str(_buffer))
        start = _b+1

        time.sleep(10)
        print((end/len(buffer))*100)
    time.sleep(120)
    mqtt_client.publish(pic_feed, '##########################################')
    print('DONE')
    mqtt_client.publish(temperature_feed, cpu_temp)
    #print("Published!")
    j= 1 + i
lights.ToggleLight('White')

import lights
import internet

import os, ssl, socketpool, wifi
import adafruit_minimqtt.adafruit_minimqtt as MQTT

internet.ConnectToWifi()

#Create a socket pool
pool = socketpool.SocketPool(wifi.radio)

#Get adafruit io username and key from settings.toml
aio_username = os.getenv('AIO_USERNAME')
aio_key = os.getenv('AIO_KEY')

#Setup a feed: This may have a different name tha you Dashboard
strip_on_off_feed = aio_username + "/feeds/strip_on_off"

#Setup functions to respond to MQTT events

def connected(client, userdata, flags, rc):
    # Connected to broke at adafruit io
    print("Connected to Adafruit IO! Listening for topic changes I have subscribed to")
    #Subscribe to all changes on the feed
    client.subscribe(strip_on_off_feed)
    
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

print("Connecting to Adafruit IO...")
mqtt_client.connect()
lights.ToggleLight('White')
j = 0
i = 10
while j <= i:
    #keep checking the mqtt message queue
    mqtt_client.loop()
    j+= 1
    #If you had other non mqtt code, you coul add it here
lights.ToggleLight('White')
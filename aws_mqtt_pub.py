# Import packages
import paho.mqtt.client as mqtt
import time
import threading
import sensortag

# Define Variables
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 30
MQTT_HOST = "192.168.0.1"
MQTT_TOPIC = "sensortag/sensors"


# Define callback function for publishing
def on_publish(client, userdata, mid):
	print("A message published successfully!")


def connect_tag(mac_address=None):
   
    if mac_address:
        tag=sensortag.SensorTag(mac_address)
        print('connected to {}'.format(mac_address))
        
        return tag


def enable_temperature_humidity_battery_sensors(object):
    #Enable temperature sensor
    object.IRtemperature.enable()
    #Enable humidity sensor
    object.humidity.enable()
    #Enable battery sensor
    object.battery.enable()
    #Waiting for sending data from sensor
    time.sleep(1)
    
  
def read_data(object):
    enable_temperature_humidity_battery_sensors(object)
    
    while True:
        MQTT_MSG='Tag {0}: Temperature is {1}, Humidity is {2}, Battery is {3}%'.format(object.macaddress,object.IRtemperature.read()[1],object.humidity.read()[1],object.battery.read())
        # Publish Sensor info
        mqttc.publish(MQTT_TOPIC,MQTT_MSG,qos=0)
        object.waitForNotifications(1.0)    


# Initiate MQTT Client
mqttc = mqtt.Client()
# Register publish callback function
mqttc.on_publish = on_publish
# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)		
mqttc.loop_start()


tags=[]
tags.append(connect_tag('54:6C:0E:53:12:0A'))
tags.append(connect_tag('54:6C:0E:80:5A:81'))    


for tag in tags:
    threading.Thread(target=read_data,args=(tag,)).start()	
   



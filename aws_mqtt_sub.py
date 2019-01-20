# Import packages
import paho.mqtt.client as mqtt
import time
import ssl

# Define Variables
AWS_MQTT_PORT = 8883
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 30
MQTT_TOPIC = "sensortag/sensors"


# Cloud Configuration (Host, Certification file, Private Key)
AWS_MQTT_HOST = "aoscy1wztqxzf.iot.ap-southeast-1.amazonaws.com"
# Local host
MQTT_HOST = "192.168.0.1"
CA_ROOT_CERT_FILE = "/home/leh08/root-CA.crt"
THING_CERT_FILE = "/home/leh08/MyCertificate.pem.crt"
THING_PRIVATE_KEY = "/home/leh08/MyPrivate.pem.key"


# Define on connect event function
# Subscribe to our Topic in this function
def on_connect(mosq, obj, flags, rc):
    mqttc.subscribe(MQTT_TOPIC, 0)


# Define on_message event function. 
# This function will be invoked every time,
# a new message arrives for the subscribed topic 
def on_message(mosq, obj, msg):
    print("=========================================================================")
    print("Topic: " + msg.topic)
    print("QoS: " + str(msg.qos))
    print("Payload: " + msg.payload.decode("UTF-8"))
    print("=========================================================================")
    mqttc.publish(MQTT_TOPIC,msg.payload.decode("UTF-8"),qos=0)
    time.sleep(1)

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed Topics : " + 
          MQTT_TOPIC + "," + " with QoS: " + str(granted_qos))
    print("=========================================================================")


def on_publish(client, userdata, mid):
	print("A message published successfully!")
    

# Initiate MQTT Client
mqttc1 = mqtt.Client()
# Register callback functions
mqttc1.on_subscribe = on_subscribe
mqttc1.on_message = on_message
# Connect with MQTT Broker
mqttc1.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
mqttc1.subscribe(MQTT_TOPIC, 0)
mqttc1.loop_start()

# Initiate MQTT Client
mqttc = mqtt.Client()

# Register callback functions
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_publish = on_publish

# Configure TLS Set
mqttc.tls_set(CA_ROOT_CERT_FILE, certfile=THING_CERT_FILE, keyfile=THING_PRIVATE_KEY, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
# Connect with MQTT Broker
mqttc.connect(AWS_MQTT_HOST,AWS_MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
mqttc.loop_start()

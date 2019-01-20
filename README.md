# Raspberry Pi with AWS IoT platform
How to interact between AWS IoT platform and Raspberry-Pi, also between SensorTag and Raspberry Pi

## Introduction
'''This project aims to connect SensorTag and utilize its state of the art of sensors to collect data/information from environment and publish to MQTT Broker which act as a transfer point before publishing to AWS MQTT IoT Cloud'''
> Send a message/information from SensorTag(Temperature, Humiditty, Battery levels) to Raspberry Pi.
> Raspberry Pi decodes raw information with formulas and pulish it to local MQTT broker
> Local MQTT broker receives messages from its clients and publish those message to AWS MQTT Broker (AWS IoT)

## Environment
* Device: Raspberry Pi, SensorTag
* Programming: Python 3.6
* Cloud Server: AWS IoT
* Protocol: MQTT, Http

## Import libraries
* Paho : MQTT Client library for python > `pip install paho-mqtt`
* Bluepy: 'sudo apt-get install python3-pip libglib2.0-dev'
	  'pip install install bluepy'
* Sensortag.py module: Download link 'https://github.com/IanHarvey/bluepy/blob/master/bluepy/sensortag.py'
* ssl : security
* time : time.sleep()
* Access to your AWS IAM to create CA certificate, and generate pair keys using for establish TLS connection. https://aws.amazon.com/iam/

## Code Description
* aws_mqtt_pub.py: This is for publishing information it receive from SensorTag and publish it to MQTT Broker (in this project, Router also act as MQTT broker to receive all local information before publish them to AWS MQTT broker). This needs to set your own `local MQTT broker address` 

* aws_mqtt_sub.py: This is for subscribe topic it want to revceive to local MQTT broker. The file also connect have connect function help to establish connections between MQTT client and MQTT broker. So that it can collect messages and publish to AWS MQTT broker. 

* sensortag.py: A sensortag module based on the module bluepy that help Raspberry Pi establish connections between SensorTags and Raspberry Pi. The sensortag module provides algorithms to MQTT client to decode data from SensorTag to be human readable data and correct the information, in other words to eliminate noises. 

## Created by Unha Back, Giang Hoang Le, Wennan Shi

## References
* AWS Connecting Raspberry Pi: https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdk-setup.html

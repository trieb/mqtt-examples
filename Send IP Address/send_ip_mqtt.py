#!/usr/bin/python3
import time
from datetime import datetime
import urllib.request
import json
import paho.mqtt.client as mqtt

DEBUG = False

# Config params
broker_address = "<broker address>"
subscribe_topic = "<topic>"
publish_topic = "<topic to publish on on>"

def getIP():
	request  = urllib.request.Request('http://httpbin.org/ip')
	response = urllib.request.urlopen(request)
	#obj = json.load(response)
	str_response = response.readall().decode('utf-8')
	obj = json.loads(str_response)
	return obj['origin']

def on_connect(client, userdata, rc):
	if(DEBUG):
		print("Connected to broker")
	client.subscribe(subscribe_topic)

def on_message(client, userdata, msg):
	if(DEBUG):
		print("Received message")
	print(msg.topic, ": ", str(msg.payload))

# Initiate mqtt-client
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect(broker_address, 1883, 60)
mqttc.loop_start()

running = True

while running:
	# Get the external IP
	IP = getIP()
	if(DEBUG):
		print(IP)
	mqttc.publish(publish_topic, IP, qos=0, retain=True)
	
	time.sleep(5)
	mqttc.loop_stop()
	running = False
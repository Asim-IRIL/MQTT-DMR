import paho.mqtt.client as mqtt
from Store import sensor_Data_Handler

MQTT_Broker = "192.168.0.113"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "Home/BedRoom/#"

def on_connect(self, mosq, obj, rc):
	self.subscribe(MQTT_Topic, 0)
	print("rc: " + str(rc))

def on_message(mosq, obj, msg):
	print "MQTT Data Received..."
	print "MQTT Topic: " + msg.topic  
	print "Data: " + msg.payload
	sensor_Data_Handler(msg.topic, msg.payload)

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

def on_log(mosq, obj, level, string):
    print(string)

mqttc = mqtt.Client("Sub_DMR")
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_log = on_log

mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
mqttc.loop_forever()

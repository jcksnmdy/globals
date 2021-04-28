import paho.mqtt.publish as publish
 
MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"
 
publish.single(MQTT_PATH, "3", hostname=MQTT_SERVER)
 
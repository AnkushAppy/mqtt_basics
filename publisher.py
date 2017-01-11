import paho.mqtt.client as mqtt
import json
import datetime

msg = [{
	"topic":"hello/world",
	"payload":"Hell! Yeah"
}]

msg1 = {
	"latitude":12.823742,
	"longitude":77.34324,
	"timestamp": datetime.datetime.now().isoformat()
}

mqttc = mqtt.Client()
mqttc.connect("54.254.209.56", 1883)
mqttc.publish("owntracks/kinzie", json.dumps(msg1))
mqttc.publish("owntracks/owntracks/kinzie", json.dumps(msg1))
mqttc.loop(2)
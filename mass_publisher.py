import paho.mqtt.client as mqtt
import json
import datetime
import random
import time

mqttc = mqtt.Client()
mqttc.connect("54.254.209.56", 1883)
i = 0
while mqttc.loop() == 0:
    i += 1
    msg1 = {
        "latitude": random.uniform(12.5, 12.9),
        "longitude": random.uniform(77.5, 77.9),
        "timestamp": datetime.datetime.now().isoformat()
    }
    mqttc.publish("owntracks/kinzie", json.dumps(msg1))
    mqttc.publish("owntracks/owntracks/kinzie", json.dumps(msg1))
    time.sleep(0.01)
    print i

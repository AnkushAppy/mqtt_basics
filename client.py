import paho.mqtt.client as mqtt
import json
# import sqlite3
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# cursor.execute('''
#     CREATE TABLE location (id INTEGER PRIMARY KEY, lat Float, lon Float, time datetime
#                        phone TEXT, email TEXT unique, password TEXT)
# ''')

print "Opened database successfully";

def on_connect(client, userdata, flags, rc):
	print "on_connect"
	print client, userdata, flags, rc
	client.subscribe("owntracks/kinzie")
	print "subscribed"

def on_message(client, userdata, msg):

	json_data = json.loads(msg.payload)

	lat = json_data.get('latitude')
	lon = json_data.get('longitude')
	time_stamp = json_data.get('timestamp')

	with open('lat_lon','a') as f:
		f.write("{0},{1},{2}\n".format(lat,lon,time_stamp))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(host='54.254.209.56',
			   port=1883
			   )
client.loop_forever()

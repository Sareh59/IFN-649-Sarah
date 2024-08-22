#publish topic:

import paho.mqtt.publish as publish

publish.single("ifn649", "Hello World", hostname="52.87.170.192")
print("Done")



#Subscrib

import paho.mqtt.client as mqtt

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT with result code " + str(rc))
    # Subscribe to the topic where the Raspberry Pi is publishing humidity data
    client.subscribe("sensor/humidity")

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {str(msg.payload.decode())}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker on the AWS server
client.connect("52.87.170.192", 1883, 60)

# Start the loop to process received messages
client.loop_forever()

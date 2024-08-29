import paho.mqtt.client as mqtt
import serial

# Define the callback for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT")
    print("Connection returned result: " + str(rc))
    client.subscribe("ifn649")  # Subscribe to the topic "ifn649"

# Define the callback for when a message is received from the broker
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    
    # Open a serial connection to the Bluetooth device
    ser = serial.Serial("/dev/rfcomm0", 9600)
    
    # Write the received MQTT message to the serial port
    ser.write(msg.payload)
    ser.close()  # Close the serial connection after sending the message

# Create an MQTT client instance
client = mqtt.Client()

# Assign the callbacks to the client
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect("52.87.170.192", 1883, 60)

# Start the network loop and keep it running to listen for messages
client.loop_forever()

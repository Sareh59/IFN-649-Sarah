import paho.mqtt.client as mqtt
import serial

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT")
    print("Connection returned result: " + str(rc))
    client.subscribe("ifn649")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    try:
        ser = serial.Serial("/dev/rfcomm0", 9600)  # Adjust the serial port as necessary
        ser.write(msg.payload)  # Send the actual message via Bluetooth
        ser.close()  # Close the serial connection
        print("Message sent to Bluetooth")
    except Exception as e:
        print(f"Error sending message to Bluetooth: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("52.87.170.192", 1883, 60)
client.loop_forever()

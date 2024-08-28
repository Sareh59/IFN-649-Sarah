
import paho.mqtt.publish as publish

# Function to publish a message
def publish_command(command):
    publish.single("ifn649", command, hostname="52.87.170.192")
    print(f"Published command: {command}")

# Allow user to input a command
command = input("Enter a command to send (e.g., LED_ON, LED_OFF): ")
publish_command(command)

 
"""EE 250L Lab 04 Starter Code
Run vm_sub.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time


"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    client.subscribe("kamody/ping")
    client.message_callback_add("kamody/ping", on_message_from_ping) 


def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

def on_message_from_ping(client, userdata, message): 
   print("Custom callback  - Ping: "+message.payload.decode())

   message = int(message.payload.decode()) + 1

   time.sleep(2)

   client.publish("kamody/pong", f"{message}") 

   print("Publishing pong value")

if __name__ == '__main__':
    client = mqtt.Client()
    
   
    client.on_message = on_message

    client.on_connect = on_connect


    client.connect(host="192.168.2.47", port=1883, keepalive=60) 


    time.sleep(1)


    client.loop_forever()

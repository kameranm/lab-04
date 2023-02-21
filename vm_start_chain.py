

from multiprocessing.sharedctypes import Value
import paho.mqtt.client as mqtt
import time

# similar to vm sub py, just changed so it receives and sends ip/ping message
"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    time.sleep(1)
    client.subscribe("kamody/pong") 

    client.message_callback_add("kamody/pong", on_message_from_pong) 

    client.publish("kamody/ping", 13)


def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

def on_message_from_pong(client, userdata, message): 
   print("Custom callback  - Pong: "+(message.payload.decode()))
   value= int(message.payload.decode()) + 1
   time.sleep(2)
   client.publish("kamody/ping", f"{value}") 
   print("Publishing ping value")

if __name__ == '__main__':
  
    client = mqtt.Client()
    
    client.on_message = on_message

    client.on_connect = on_connect


    client.connect(host="192.168.2.47", port=1883, keepalive=60)
    
    time.sleep(1)
    client.loop_forever()

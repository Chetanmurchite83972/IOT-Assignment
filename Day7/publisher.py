import paho.mqtt.client as mqtt

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Test")

def on_publish(client, userdata, mid, reason_code, properties):
    print("Message is published successfully")

mqttc.on_publish = on_publish

mqttc.connect(host="localhost")

mqttc.publish("sensor/ldr","50", qos=1)

print("message send sucessfully")
mqttc.disconnect()

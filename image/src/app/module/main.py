"""
All logic related to the module's main application
Mostly only this file requires changes
"""

import paho.mqtt.client as mqtt
import json

from app.config import APPLICATION

# create MQTT client
client = mqtt.Client()

# connect the client to a remote MQTT broker
try:
    print("Connecting to MQTT... Broker: %s Port: %s", APPLICATION["MQTT_BROKER"], APPLICATION["PORT"])
    client.connect(host=APPLICATION['MQTT_BROKER'], port=APPLICATION['PORT'])
    print("Successfully connected to MQTT Broker!")
except Exception:
    print("Error: Cannot establish connection to a remote MQTT broker. Check provided MQTT broker address or port.")

# define labels for data egressed through MQTT
if APPLICATION['LABELS']:
    LABELS = [label.strip() for label in APPLICATION['LABELS'].split(',')]
else:
    LABELS = None

def module_main(data):
    """
    Receive data and send to a remote MQTT broker.

    Args:
        data ([JSON Object]): [Data received by the module and validated by data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    try:
        # build return body
        if type(data) == dict:
            return_body = processData(data)
        else:
            return_body = []
            for data_instance in data:
                return_body.append(processData(data_instance))

        # publish data to a remote MQTT broker
        result = client.publish(topic=APPLICATION['TOPIC'], payload=json.dumps(return_body), qos=APPLICATION['QOS'])

        # result: [0, 1]
        if result[0] == 0:
            # successful publishing
            return data, None
        else:
            return None, "Failed to send message to MQTT topic."

    except Exception:
        return None, "Unable to perform the module logic"

def processData(parsed_data):
    return_body = {}
    if LABELS:
        for label in LABELS:
            # check if selected input label is in input data
            if label in parsed_data.keys():
                return_body[label] = parsed_data[label]
    else:
        return_body = parsed_data

    return return_body
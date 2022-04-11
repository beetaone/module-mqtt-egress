"""
All logic related to the module's main application
Mostly only this file requires changes
"""

import paho.mqtt.client as mqtt
import time

from app.config import APPLICATION

# create MQTT client
client = mqtt.Client()

# define labels for data egressed through MQTT
if APPLICATION['LABELS']:
    LABELS = [label.strip() for label in APPLICATION['LABELS'].split(',')]
else:
    LABELS = None

def connect_client():
    """
    Connects to a remote MQTT broker.

    Returns:
        None: if successfully connected to MQTT broker.
        Error: if connections fails.
    """
    try:
        # connect the client to a remote MQTT broker
        client.connect(host=APPLICATION['MQTT_BROKER'], port=APPLICATION['PORT'])

        return None
    except Exception:
        return "Cannot establish connection to a remote MQTT broker. Check provided MQTT broker address or port."

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
            for data in data:
                return_body.append(processData(data))

        # publish data to a remote MQTT broker
        client.publish(topic=APPLICATION['TOPIC'], payload=return_body, qos=APPLICATION['QOS'])

        return data, None
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

    # add timestamp
    if not APPLICATION['TIMESTAMP']:
        return_body['timestamp'] = time.time()
    else:
        return_body = removekey(return_body, APPLICATION['TIMESTAMP'])
        return_body['timestamp'] = parsed_data[APPLICATION['TIMESTAMP']]
    return return_body

def removekey(d, key):
    r = dict(d)
    if not key in d:
        return r
    del r[key]
    return r
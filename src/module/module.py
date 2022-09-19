"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

import paho.mqtt.client as mqtt
import json
import sys

from logging import getLogger
from .params import PARAMS

log = getLogger("module")

# create MQTT client
client = mqtt.Client()

# connect the client to a remote MQTT broker
__MQTT_BROKER__ = PARAMS['MQTT_BROKER']
if '://' in __MQTT_BROKER__:
    protocol = __MQTT_BROKER__.split('://')[0]
    if protocol != 'mqtt':
        log.error(f'Unsupported broker URL protocol {protocol}. Please provide URL with mqtt:// protocol.')
        # kill the process
        sys.exit(1)
    else:
        __MQTT_BROKER__ = __MQTT_BROKER__.replace('mqtt://', '')
log.debug(f'Connecting to MQTT... Broker: {__MQTT_BROKER__} Port: {PARAMS["PORT"]}')
client.connect(host=__MQTT_BROKER__, port=PARAMS['PORT'])
log.debug('Successfully connected to MQTT Broker!')

# define labels for data egressed through MQTT
if PARAMS['LABELS']:
    LABELS = [label.strip() for label in PARAMS['LABELS'].split(',')]
else:
    LABELS = None

def module_main(received_data: any) -> str:
    """
    Receive data and send to a remote MQTT broker.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Outputting ...")

    try:
        # YOUR CODE HERE

        # build return body
        if type(received_data) == dict:
            return_body = processData(received_data)
        else:
            return_body = []
            for data_instance in received_data:
                return_body.append(processData(data_instance))

        # publish data to a remote MQTT broker
        rc, _ = client.publish(topic=PARAMS['TOPIC'], payload=json.dumps(return_body), qos=PARAMS['QOS'])

        if rc == mqtt.MQTT_ERR_SUCCESS:
            # successful publishing
            return None
        else:
            return 'Failed to send a message to MQTT topic.'

    except Exception as e:
        return f"Exception in the module business logic: {e}"

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

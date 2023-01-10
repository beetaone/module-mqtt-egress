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

client = mqtt.Client()

# extract the protocol and host from the MQTT broker URL
__MQTT_BROKER__ = PARAMS['MQTT_BROKER']
if '://' in __MQTT_BROKER__:
    protocol, host = __MQTT_BROKER__.split('://')
else:
    protocol, host = "mqtt", __MQTT_BROKER__


log.debug(f'Protocol: {protocol} Host: {host}')

# check if the protocol is supported
supported_protocols = ['mqtt', 'ws']
if protocol not in supported_protocols:
    log.error(f'Unsupported broker URL protocol {protocol}. Please provide URL with a supported protocol: {supported_protocols}')
    sys.exit(1)

# set the protocol to use for the connection based on the provided protocol
if protocol == 'ws':
    client.ws_set()

# extract the port from the PARAMS dictionary
port = PARAMS['PORT']

# connect the client to the MQTT broker
log.info(f'Connecting to MQTT... Broker: {host} Port: {port}')
client.connect(host=host, port=port)

# log a success message
log.info('Successfully connected to MQTT Broker!')


# define labels for data egressed through MQTT
# define labels for data egressed through MQTT
LABELS = PARAMS.get('LABELS', '').strip().split(',') if PARAMS.get('LABELS', '') else None


def module_main(received_data: any) -> str:
    """
    Receive data and send to a remote MQTT broker.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    try:
        return_body = processData(received_data) if isinstance(received_data, dict) else [processData(data_instance) for data_instance in received_data]

        log.debug(f"Sending data to MQTT topic: {PARAMS['TOPIC']}")
        log.debug(f"Data: {return_body}")

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
    """
    If the LABELS variable is defined, return a dictionary of the parsed data with only the keys in
    LABELS. Otherwise, return the parsed data.

    :param parsed_data: The data that was parsed from the log file
    :return: A dictionary of the parsed data.
    """
    if LABELS:
        return {label: parsed_data[label] for label in LABELS if label in parsed_data}
    return parsed_data

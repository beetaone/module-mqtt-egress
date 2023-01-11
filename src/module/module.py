"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

import json
import sys
from logging import getLogger

import paho.mqtt.client as mqtt
from paho.mqtt.packettypes import PacketTypes
from paho.mqtt.properties import Properties

from .mqtt_client import MqttClient
from .params import PARAMS

log = getLogger("module")

mqtt_client = MqttClient.get_instance()
client = mqtt_client.client

properties = Properties(PacketTypes.PUBLISH)
properties.MessageExpiryInterval = 30  # in seconds

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
        if not client.is_connected:
            log.debug("Reconnecting...")
            client.reconnect()
            log.debug("Reconnected succesfully")

        rc, _ = client.publish(topic=PARAMS['TOPIC'], payload=json.dumps(return_body), qos=PARAMS['QOS'], retain=PARAMS['RETAIN'], properties=properties)

        if rc == mqtt.MQTT_ERR_SUCCESS:
            log.debug("Data sent successfully.")
            return None
        else:
            return f"Failed to send a message to MQTT topic. Return code: {rc}"

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

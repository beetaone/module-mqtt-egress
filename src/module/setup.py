import sys
from logging import getLogger
from .mqtt_client import MqttClient

from .params import PARAMS

log = getLogger("setup")
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


def setup_module():
    mqtt_client = MqttClient.get_instance()
    client = mqtt_client.client
    # set the protocol to use for the connection based on the provided protocol
    if protocol == 'ws':
        client.ws_set()
    port = PARAMS['PORT']
    log.info(f'Connecting to MQTT... Broker: {host} Port: {port}')
    client.connect(host=host, port=port)
    log.info('Successfully connected to MQTT Broker!')

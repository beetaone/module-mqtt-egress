import paho.mqtt.client as mqtt

from logging import getLogger
import random
import string


log = getLogger("mqtt_client")

client_id = ''.join(random.choices(string.ascii_letters + string.digits, k=10))


class MqttClient:
    _instance = None

    def __init__(self):
        self.client = mqtt.Client(client_id=client_id, clean_session=True)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_socket_open = self.on_socket_open
        self.client.on_socket_close = self.on_socket_close

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            log.info("Connected to MQTT broker")
        else:
            log.error("Failed to connect to MQTT broker. Return code: {}".format(rc))

    def on_disconnect(self, client, userdata, rc):
        log.info("Disconnected from MQTT broker. Return code: {}".format(rc))

    def on_socket_open(self, client, userdata, sock):
        log.info("Successfully opened a socket connection to MQTT broker")

    def on_socket_close(self, client, userdata, sock):
        log.warning("Socket connection to MQTT broker closed")

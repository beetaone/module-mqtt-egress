from os import getenv

PARAMS = {
    "MQTT_BROKER": getenv("MQTT_BROKER", "mqtt://test.mosquitto.org"),
    "PORT": int(getenv("PORT", 1883)),
    "TOPIC": getenv("TOPIC", "weeve/factory"),
    "QOS": int(getenv("QOS", 0)),
    "LABELS": getenv("LABELS", ""),
}

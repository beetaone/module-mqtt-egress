from os import getenv

PARAMS = {
    "MQTT_BROKER": getenv("MQTT_BROKER", "test.mosquitto.org"),
    "PORT": int(getenv("PORT", 1883)),
    "TOPIC": getenv("TOPIC", "beetaone/factory"),
    "RETAIN": getenv("RETAIN", "false").lower() == "true",
    "QOS": int(getenv("", 0)),
    "LABELS": getenv("LABELS", ""),
}
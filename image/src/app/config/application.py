"""
All constants specific to the application
"""
from app.utils.env import env
from app.utils.intenv import intenv

APPLICATION = {
    "MQTT_BROKER": env("MQTT_BROKER", "127.0.0.1"),
    "PORT": intenv("PORT", 1883),
    "TOPIC": env("TOPIC", "weeve/factory"),
    "QOS": intenv("QOS", 0),
    "LABELS": env("LABELS", ""),
    "TIMESTAMP": env("TIMESTAMP", "")
}

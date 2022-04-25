"""
All constants specific to the application
"""
import os
from app.utils.intenv import intenv

APPLICATION = {
    "MQTT_BROKER": os.getenv("MQTT_BROKER", "mqtt://test.mosquitto.org"),
    "PORT": intenv("PORT", 1883),
    "TOPIC": os.getenv("TOPIC", "weeve/factory"),
    "QOS": intenv("QOS", 0),
    "LABELS": os.getenv("LABELS", ""),
}

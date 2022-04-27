"""
All constants specific to weeve
"""
import os

WEEVE = {
    "MODULE_NAME": os.getenv("MODULE_NAME", "mqtt-egress"),
    "MODULE_TYPE": os.getenv("MODULE_TYPE", "EGRESS"),
    "EGRESS_SCHEME": os.getenv("EGRESS_SCHEME", "http"),
    "EGRESS_HOST": os.getenv("EGRESS_HOST", "localhost"),
    "EGRESS_PORT": os.getenv("EGRESS_PORT", "80"),
    "EGRESS_PATH": os.getenv("EGRESS_PATH", ""),
    "EGRESS_URL": os.getenv("EGRESS_URL", ""),
    "INGRESS_HOST": os.getenv("INGRESS_HOST", "0.0.0.0"),
    "INGRESS_PORT": os.getenv("INGRESS_PORT", "80"),
    "INGRESS_PATH": os.getenv("INGRESS_PATH", "")
}

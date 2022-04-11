"""Main app file"""
from logging import getLogger
from app import create_app
from app.config import WEEVE, configure_logging, APPLICATION
from app.module import connect_client


log = getLogger("main")


def main():
    """ Main app entry point"""
    configure_logging()
    log.info("%s Started", WEEVE["MODULE_NAME"])

    log.info("Connecting to MQTT... Broker: %s Port: %s", APPLICATION["MQTT_BROKER"], APPLICATION["PORT"])
    err = connect_client()
    if err:
        log.error("Error: %s", err)
    else:
        log.info("Successfully connected to MQTT Broker!")

    app = create_app()
    app.run(host=WEEVE['INGRESS_HOST'], port=WEEVE["INGRESS_PORT"])


if __name__ == "__main__":
    main()

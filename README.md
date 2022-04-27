# MQTT Egress


|              |                                                                   |
| ------------ | ----------------------------------------------------------------- |
| name         | MQTT-Egress                                                       |
| version      | v0.0.1                                                            |
| docker image | [weevenetwork/mqtt-egress](https://hub.docker.com/r/weevenetwork/mqtt-egress)        |
| tags         | Python, Flask, Docker, Weeve, MQTT, Egress                        |
| authors      | Jakub Grzelak                                                     |

***

- [MQTT Egress](#mqtt-egress)
  - [Description](#description)
  - [Features](#features)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)
  - [Docker Compose Example](#docker-compose-example)

***



## Description

MQTT Egress is an output module responsible for publishing data to a selected MQTT broker and topic.

## Features

* Publish to MQTT Broker
* Egresses data out of the data service

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:


| Name                | Environment Variables | Type    | Description                |
| ------------------- | --------------------- | ------- | -------------------------- |
| MQTT Broker Address | MQTT_BROKER           | string  | eg: test.mosquitto.org     |
| Connection Port     | PORT                  | integer | Port number for the broker |
| Topic               | TOPIC                 | string  | Topic to publish         |
| Quality of Service  | QOS                   | integer | Quality of Service         |
| Input Labels        | LABELS                | string  | List of comma (,) separated labels to read from a previous module. Leave empty ("") to keep all data. |

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

### Set by the weeve Agent on the edge-node

| Environment Variables | type   | Description                            |
| --------------------- | ------ | -------------------------------------- |
| EGRESS_URL            | string | HTTP ReST endpoint for the next module |
| MODULE_NAME           | string | Name of the module                               |
| MODULE_TYPE           | string | Type of the module (ingress, processing, egress) |
| INGRESS_HOST          | string | Host to which data will be ingressed             |
| INGRESS_PORT          | string | Port to which data will be ingressed             |
| INGRESS_PATH          | string | Path to which data will be ingressed             |




## Dependencies

```txt
Flask
requests
python-dotenv
paho-mqtt
```

## Input

Input to this module is JSON body single object or array of objects:

Example:

```node
{
  temperature: 15,
}
```

```node
[
  {
    temperature: 15,
  },
  {
    temperature: 21,
  },
  {
    temperature: 25,
  },
];
```

## Output

Output of this module is identical JSON body as input that is sent to a chosen endpoint.

Example:

```node
{
  temperature: 15,
}
```

```node
[
  {
    temperature: 15,
  },
  {
    temperature: 21,
  },
  {
    temperature: 25,
  },
];
```

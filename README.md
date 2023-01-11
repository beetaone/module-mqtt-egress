# MQTT Egress

|           |                                                                               |
| --------- | ----------------------------------------------------------------------------- |
| Name      | MQTT Egress                                                                   |
| Version   | v1.0.0                                                                        |
| DockerHub | [weevenetwork/mqtt-egress](https://hub.docker.com/r/weevenetwork/mqtt-egress) |
| authors   | Jakub Grzelak                                                                 |

- [MQTT Egress](#mqtt-egress)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

MQTT Egress is an output module responsible for publishing data to a selected MQTT broker and topic.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                | Environment Variables | Type    | Description                                                                                           |
| ------------------- | --------------------- | ------- | ----------------------------------------------------------------------------------------------------- |
| MQTT Broker Address | MQTT_BROKER           | string  | eg: test.mosquitto.org                                                                                |
| Connection Port     | PORT                  | integer | Port number for the broker                                                                            |
| Topic               | TOPIC                 | string  | Topic to publish                                                                                      |
| Quality of Service  | QOS                   | integer | Quality of Service                                                                                    |
| Retain              | RETAIN                | boolean | Retain the message                                                                                    |
| Input Labels        | LABELS                | string  | List of comma (,) separated labels to read from a previous module. Leave empty ("") to keep all data. |


### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output) |
| INGRESS_HOST          | string | Host to which data will be ingressed           |
| INGRESS_PORT          | string | Port to which data will be ingressed           |

## Dependencies

```txt
bottle
requests
paho-mqtt
```

## Input

Input to this module is JSON body single object or array of objects:

Example:

```json
{
  temperature: 15,
}
```

```json
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

```json
{
  temperature: 15,
}
```

```json
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

import json
import paho.mqtt.client as mqtt


class MQTTAdapter:
    def __init__(self, broker_url: str = "localhost", port: int = 1883):
        self.broker = broker_url
        self.port = port
        self.client = mqtt.Client()

    def connect(self):
        self.client.connect(self.broker, self.port)

    def send_command(self, topic: str, payload: dict):
        self.client.publish(topic, json.dumps(payload))


import os
import json
import datetime

import pika

import helper

# MQ_HOST = os.environ.get("MQ_HOST")
MQ_HOST = "rabbitmq"


class MqClient(object):
    def __init__(self):
        credentials = pika.PlainCredentials("system", "system")
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=MQ_HOST, credentials=credentials)
        )
        self.channel = self.connection.channel()

    def publish(self, queue, data):
        self.channel.queue_declare(queue=queue, durable=True)
        self.channel.basic_publish(
            exchange="", routing_key=queue, body=json.dumps(data)
        )

    def publish_sensor_state(self, mac, temp, humidity, battery):
        data = {
            "mac": mac,
            "temp": temp,
            "humidity": humidity,
            "battery": battery,
            "timestamp": helper.dt.now(),
        }

        self.publish("sensor_state", data)

    def publish_sensor_request(self, mac):
        data = {
            "mac": mac,
        }

        self.publish("sensor_request", data)

    def consuming(self, queue, callback):
        self.channel.queue_declare(queue=queue, durable=True)

        self.channel.basic_consume(
            on_message_callback=callback, queue=queue
        )
        self.channel.start_consuming()

    def close(self):
        self.channel.close()
        self.connection.close()

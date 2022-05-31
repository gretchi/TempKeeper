
import os
import logging
import time
import json
import random
import subprocess

from blesensor import Sensor

from consumer_base import ConsumerBase
import helper
from mq_client import MqClient

DEVELOP = os.environ.get("DEVELOP")
QUEUE_NAME = "sensor_request"


class TemperatureCollectionConsumer(ConsumerBase):
    def __init__(self):
        super().__init__()

        self._dummy_device = {}
        self.set_queue(QUEUE_NAME)

    def callback(self, ch, method, properties, body):
        json_body = json.loads(body.decode("utf-8"))
        mac = json_body.get("mac")
        try:
            self.bt_work(mac)
        except Exception as e:
            logging.critical(e)
            subprocess.run(
                [
                    "reboot now"
                ]
            )

        ch.basic_ack(delivery_tag=method.delivery_tag)

    def bt_work(self, mac):
        if DEVELOP == "1":
            temp, humidity, battery = self.dummy_device_function(mac)

        else:
            sensor = Sensor(mac)
            sensor.scan(timeout=20)

            temp = sensor.get("Temperature")
            humidity = sensor.get("Humidity")
            battery = sensor.get("BatteryVoltage")

        logging.info(
            f"mac: {mac}, temp: {temp}, humidity: {humidity}, battery: {battery}")
        self.mq.publish_sensor_state(mac, temp, humidity, battery)

        time.sleep(10)

        return

    def dummy_device_function(self, mac):
        if mac in self._dummy_device:
            dummy_temp = self._dummy_device[mac]["temp"]
            dummy_humidity = self._dummy_device[mac]["humidity"]
        else:
            dummy_temp = 25
            dummy_humidity = 50

        dummy_temp += random.uniform(-0.5, 0.5)
        dummy_humidity += random.uniform(-0.5, 0.5)

        dummy_temp = min(dummy_temp, 30)
        dummy_temp = max(dummy_temp, 20)
        dummy_humidity = min(dummy_humidity, 60)
        dummy_humidity = max(dummy_humidity, 40)

        self._dummy_device[mac] = {
            "temp": dummy_temp,
            "humidity": dummy_humidity,
        }
        temp = int(dummy_temp)
        humidity = int(dummy_humidity)
        battery = 100

        return temp, humidity, battery

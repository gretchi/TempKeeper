
import os
import logging
import time
import random
import datetime

from .blesensor import Sensor

import helper

DOCKER = os.environ.get("DOCKER")


class BTWork(object):
    def __init__(self, mac):
        self.mac = mac
        self._dummy_device = {}

    def scan(self):
        if DOCKER == "1":
            temp, humidity, battery = self.dummy_device_function(self.mac)

        else:
            sensor = Sensor(self.mac)
            sensor.scan(timeout=20)

            temp = sensor.get("Temperature")
            humidity = sensor.get("Humidity")
            battery = sensor.get("BatteryVoltage")

        logging.info(
            f"mac: {self.mac}, temp: {temp}, humidity: {humidity}, battery: {battery}")

        return self.mac, temp, humidity, battery, helper.dt.now()

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

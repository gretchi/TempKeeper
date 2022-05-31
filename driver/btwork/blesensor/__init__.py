from bluepy import btle

from .switchbot import SwitchbotScanDelegate

SCANNER_TIMEOUTED = 20


class Sensor(object):
    def __init__(self, mac):
        self.mac = mac
        self.scanner = btle.Scanner().withDelegate(SwitchbotScanDelegate(mac))

    def scan(self, timeout=SCANNER_TIMEOUTED):
        self.scanner.scan(timeout)

    def get(self, key):
        return self.scanner.delegate.sensorValue[key]

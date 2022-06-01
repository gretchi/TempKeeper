#!/usr/bin/env python3

import getpass
import logging

from pprint import pprint

import helper

import batch
from btwork import BTWork

FAIL_LIFE = 2

class TempCollector(batch.BatchBase):
    def __init__(self):
        self.__file__ = __file__
        super().__init__()


    def main(self):
        life = FAIL_LIFE

        for row in self.model.get_nodes_order_by_random():
            mac = row["sensor_mac"]
            location_name = row["location_name"]

            logging.info(f"Scan start location_name: {location_name}, mac: {mac}")
            btwork = BTWork(mac)
            try:
                mac, temp, humidity, battery, ts = btwork.scan()
                self.model.add_temperature(mac, temp, humidity, battery, ts)
            except Exception as e:
                logging.error(e)
                self.model.rollback()
                life -= 1
            else:
                self.model.commit()

            if life <= 0:
                raise batch.BatchSystemRebootError("Bluetooth feeling unwell")

            logging.info("end")



        return 0



if __name__ == "__main__":
    if "root" != getpass.getuser():
        logging.fatal("please run as root")
        exit(1)

    worker = TempCollector()
    exit(worker.run())

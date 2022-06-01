#!/usr/bin/env python3

import getpass
import logging

from pprint import pprint

import helper

import batch
from btwork import BTWork


class TempCollector(batch.BatchBase):
    def __init__(self):
        self.__file__ = __file__
        super().__init__()


    def main(self):
        life = 5

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

            logging.info("end")


        if life < 1:
            raise batch.BatchSystemRebootError("Bluetooth feeling unwell")

        return 0



if __name__ == "__main__":
    if "root" != getpass.getuser():
        logging.fatal("please run as root")
        exit(1)

    worker = TempCollector()
    exit(worker.run())

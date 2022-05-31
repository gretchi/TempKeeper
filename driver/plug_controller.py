#!/usr/bin/env python3

import getpass
import logging

from pprint import pprint

import helper

import batch
import plugwork

class PlugController(batch.BatchBase):
    def __init__(self):
        self.__file__ = __file__
        super().__init__()


    def main(self):
        self.search()

        for row in self.model.get_nodes():
            sensor_mac = row["sensor_mac"]
            plug_mac = row["plug_mac"]
            plug_ip = row["plug_ip"]
            preset_temp = row["preset_temp"]
            location_name = row["location_name"]

            if plug_ip is None:
                continue

            temperature = self.model.get_temperature_one(sensor_mac)
            current_temp = temperature["temp"]

            if preset_temp > current_temp:
                state = plugwork.STATE_ON
            else:
                state = plugwork.STATE_OFF

            try:
                plugwork.set_plug_state(state, plug_ip)
                self.model.add_plug_state(plug_mac, state, helper.dt.now())
            except Exception as e:
                logging.error(e)
                self.model.rollback()
            else:
                self.model.commit()


        return 0


    def search(self):
        search_result = plugwork.search()
        self.model.commit()

        for mac, plug_info in search_result.items():
            ip_addr = plug_info["ip_addr"]
            self.model.set_plug_ip(mac, ip_addr)


if __name__ == "__main__":
    if "root" != getpass.getuser():
        logging.fatal("please run as root")
        exit(1)

    worker = PlugController()
    exit(worker.run())

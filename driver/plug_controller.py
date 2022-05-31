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
            mac = row["plug_mac"]
            plug_ip = row["plug_ip"]
            location_name = row["location_name"]

            if plug_ip is None:
                continue

            print(mac, plug_ip)

        return 0


    def search(self):
        search_result = plugwork.search()
        self.model.commit()

        for mac, plug_info in search_result.items():
            ip_addr = plug_info["ip_addr"]
            self.model.set_plug_ip(mac, ip_addr)

            # ToDo: ここ
            state = plugwork.STATE_OFF

            try:
                plugwork.set_plug_state(state, ip_addr)
                self.model.add_plug_state(mac, state, helper.dt.now())
            except Exception as e:
                logging.error(e)
                self.model.rollback()
            else:
                self.model.commit()


if __name__ == "__main__":
    if "root" != getpass.getuser():
        logging.fatal("please run as root")
        exit(1)

    worker = PlugController()
    exit(worker.run())

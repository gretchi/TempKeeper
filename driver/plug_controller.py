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

        # for row in self.model.get_nodes():
        #     mac = row["plug_mac"]
        #     location_name = row["location_name"]

        return 0


    def search(self):
        search_result = plugwork.search()

        for mac, plug_info in search_result.items():
            ip_addr = plug_info["ip_addr"]
            self.model.set_plug_ip(mac, ip_addr)

        self.model.commit()


if __name__ == "__main__":
    if "root" != getpass.getuser():
        logging.fatal("please run as root")
        exit(1)

    worker = PlugController()
    exit(worker.run())

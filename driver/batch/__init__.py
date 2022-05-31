
import os
import logging

import helper
from model import Model

helper.logger.init()

class BatchBase(object):
    def __init__(self):
        self.batchname = os.path.splitext(os.path.basename(self.__file__))[0]
        self.model = Model()

    def run(self):
        logging.info(f"Start {self.batchname}")
        try:
            self.main()
        except BatchSystemRebootError as e:
            logging.critical(e)
            helper.syscmd.system_reboot()

        except Exception as e:
            logging.critical(e)

        logging.info(f"End {self.batchname}")


class BatchSystemRebootError(Exception):
    pass

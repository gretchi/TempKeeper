
import logging as sys_logging

def init():
    sys_logging.basicConfig(level=sys_logging.INFO, format="%(asctime)s [%(levelname)s] %(threadName)s: %(message)s")

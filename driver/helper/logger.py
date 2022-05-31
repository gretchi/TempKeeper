
import logging

def init():
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(threadName)s: %(message)s")

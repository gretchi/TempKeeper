
import re

def exclude_delimiter(mac):
    mac = re.sub(r"[:|-]", "", mac)

    return mac

def insert_delimiter(mac, delimiter=":"):
    mac = exclude_delimiter(mac)
    buf = ""

    for i, c in enumerate(mac):
        buf += c

        if i % 2 == 1:
            buf += delimiter

    return buf[:-1]


import re


def convert_camel(dict):
    keys = dict.copy().keys()
    for key in keys:
        value = dict[key]
        del dict[key]
        camel_key = re.sub("_(.)", lambda x: x.group(1).upper(), key)
        dict[camel_key] = value
    return dict

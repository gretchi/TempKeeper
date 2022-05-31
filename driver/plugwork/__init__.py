import os
import re
import logging

import helper

DEVELOP = os.environ.get("DEVELOP")

DUMMY_SEARCH_RESULT = """Searching...
startDiscovery({
  discoveryInterval: 2000,
  discoveryTimeout: 10000,
  breakoutChildren: true,
  broadcast: '255.255.255.255'
})
HS105(JP) plug IOT.SMARTPLUGSWITCH 10.227.12.25 9999 1027F52207C9 8006B3170134B3FBB6B7659C6852E5961EB6F50D 1-ぴー
HS105(JP) plug IOT.SMARTPLUGSWITCH 10.227.12.6 9999 1027F52208E7 8006F3CED89A307B836892FADE6D79841EB6B728 3-じん
HS105(JP) plug IOT.SMARTPLUGSWITCH 10.227.12.31 9999 AC84C6511491 8006B22686DCF8AB4BFC096D79AD62181A0FAC07 2-そら
HS105(JP) plug IOT.SMARTPLUGSWITCH 10.227.12.26 9999 1027F5220812 8006BB782B775A00E54AC84D5A9CAC641EB68C1A 5-ゆき
"""

TPLINK_SMARTHOME_API_BIN = "/usr/bin/tplink-smarthome-api"
TPLINK_HS105_MAGIC_WORD = r"^HS105\(JP\) plug IOT\.SMARTPLUGSWITCH .*$"
TPLINK_SMART_PLUG_CONTROL_PORT = 9999

STATE_OFF = 0
STATE_ON = 1

def is_develop():
    return DEVELOP == "1"

def search():
    if is_develop():
        stdout = DUMMY_SEARCH_RESULT
    else:
        stdout = helper.syscmd.execute(
            [
                TPLINK_SMARTHOME_API_BIN,
                "search"
            ]
        )

    magic_pattern = re.compile(TPLINK_HS105_MAGIC_WORD)

    search_result = {}

    for line in stdout.splitlines():
        if not magic_pattern.match(line):
            continue

        splited_line = line.split(" ")

        model = splited_line[0]
        mic_class = splited_line[1]
        mic_type = splited_line[2]
        ip_addr = splited_line[3]
        control_port = splited_line[4]
        mac_raw = splited_line[5]
        device_id = splited_line[6]
        alias = splited_line[7]
        mac = helper.net.insert_delimiter(mac_raw)

        search_result[mac] = {
            "mac": mac,
            "ip_addr": ip_addr,
            "control_port": control_port,
            "alias": alias
        }

        logging.info(f"Discover tplink smart plug: mac: {mac}, ip_addr: {ip_addr}, alias: {alias}")

    return search_result



def set_plug_state(state, host, port=TPLINK_SMART_PLUG_CONTROL_PORT):
    if state == STATE_OFF:
        cmd = '{"system":{"set_relay_state":{"state":0}}}'
    elif state == STATE_ON:
        cmd = '{"system":{"set_relay_state":{"state":1}}}'

    if is_develop():
        return

    helper.syscmd.execute(
        [
            TPLINK_SMARTHOME_API_BIN,
            "sendCommand",
            f"{host}:{port}",
            cmd,
        ]
    )

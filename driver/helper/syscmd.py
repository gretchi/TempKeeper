
import subprocess
import getpass
import logging

def system_reboot():
    if "root" != getpass.getuser():
        raise RuntimeError("please reboot command as root")

    command = ["reboot", "now"]
    execute(command)


def execute(command):
    str_command = " ".join(command)
    logging.info(f"execute subprocess command: {str_command}")

    cp = subprocess.run(command, encoding='utf-8', stdout=subprocess.PIPE)

    return cp.stdout

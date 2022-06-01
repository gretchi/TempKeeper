#!/bin/bash

cd $(dirname $0)

PYTHON_PATH="/home/gretel/.pyenv/versions/TempKeeper/bin/python"

# migration
../migration.sh

while true; do
    # sensor function
    sudo ${PYTHON_PATH} ./temp_collector.py

    # plug function
    ${PYTHON_PATH} ./plug_controller.py

    sleep 1m

done
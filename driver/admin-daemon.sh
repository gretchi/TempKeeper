#!/bin/bash

cd $(dirname $0)

PYTHON_PATH="/home/gretel/.pyenv/versions/TempKeeper/bin/python"

# migration
docker-compose exec driver alembic upgrade head

while true
    # sensor function
    sudo ${PYTHON_PATH} ./temp_collector.py

    # plug function
    ${PYTHON_PATH} ./plug_controller.py

do

done

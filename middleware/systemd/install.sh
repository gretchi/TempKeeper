#!/bin/bash

SERVICE_NAME="TempKeeper"

ln -s "/home/gretel/Git/${SERVICE_NAME}/systemd/middleware/${SERVICE_NAME}.service" "/usr/lib/systemd/system/${SERVICE_NAME}.service"

systemctl daemon-reload
systemctl enable "${SERVICE_NAME}.service"

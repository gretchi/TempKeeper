#!/bin/bash

SERVICE_NAME="TempKeeperViewer"
ln -s "/home/gretel/TempKeeper/viewer/systemd/${SERVICE_NAME}.service" "/usr/lib/systemd/system/${SERVICE_NAME}.service"
systemctl daemon-reload
systemctl enable "${SERVICE_NAME}.service"

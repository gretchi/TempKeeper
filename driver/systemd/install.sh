#!/bin/bash

SERVICE_NAME="TempKeeperAdminService"
ln -s "/home/gretel/TempKeeper/driver/systemd/${SERVICE_NAME}.service" "/usr/lib/systemd/system/${SERVICE_NAME}.service"
systemctl daemon-reload
systemctl enable "${SERVICE_NAME}.service"

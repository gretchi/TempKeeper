#!/bin/bash

SERVICE_NAME="__TEMPLATE__"

ln -s "/home/gretel/${SERVICE_NAME}/systemd/${SERVICE_NAME}.service" "/usr/lib/systemd/system/${SERVICE_NAME}.service"

systemctl daemon-reload
systemctl enable "${SERVICE_NAME}.service"

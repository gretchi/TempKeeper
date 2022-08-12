#/!bin/bash

yarn build

mkdir -p /root/static/control
cp -rpf ./dist/* /root/static/control/.

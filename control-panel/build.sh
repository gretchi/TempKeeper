#/!bin/bash

yarn build

cp -rpf ./dist/* /root/static/control/.

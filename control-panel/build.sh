#/!bin/bash

yarn add
yarn build

mkdir -p /var/www/static
cp -rpf ./dist/* /var/www/static/.

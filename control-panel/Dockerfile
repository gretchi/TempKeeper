FROM node:18-bullseye

WORKDIR /root/control-panel
RUN yarn global add @vue/cli
COPY . /root/control-panel

CMD /bin/bash ./build.sh

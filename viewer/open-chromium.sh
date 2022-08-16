#!/bin/bash

# URL="http://10.227.7.8:3000/d/HqDs-4_7k/xiao-niao-kezizhuang-tai?orgId=1&refresh=5s&kiosk=tv&from=now-24h&to=now"
URL="http://10.227.7.8:8080"

chromium "${URL}" --kiosk

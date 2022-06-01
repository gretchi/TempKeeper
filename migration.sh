#!/bin/bash

cd $(dirname $0)

docker-compose exec driver alembic upgrade head

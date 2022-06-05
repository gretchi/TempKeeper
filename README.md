# TempKeeper

令和最新版の小鳥のケージの温度を管理するソリューション！！！


## alembic

```bash
# マイグレーション
docker-compose exec driver alembic upgrade head

# 新しいリビジョンを作る
docker-compose exec driver alembic revision -m "revision_name"
```

## script

```bash
# driver
docker-compose exec driver /bin/bash -l

# temp_collector
docker-compose exec driver python3 /var/driver/temp_collector.py

# plug_controller
docker-compose exec driver python3 /var/driver/plug_controller.py
```

## pgsql

```bash
docker-compose exec pgsql psql -U system tkdb

docker-compose exec pgsql psql -U system tkdb -c "SELECT * FROM temperature ORDER BY id DESC LIMIT 10;"
docker-compose exec pgsql psql -U system tkdb -c "SELECT * FROM plug_state ORDER BY id DESC LIMIT 10;"
docker-compose exec pgsql psql -U system tkdb -c "SELECT * FROM node;"
```

```sql
SELECT * FROM temperature ORDER BY id DESC LIMIT 10;
SELECT * FROM plug_state ORDER BY id DESC LIMIT 10;
SELECT * FROM node;
```

## DB破壊

```bash
docker-compose stop pgsql && docker-compose rm pgsql && docker-compose up -d pgsql
docker-compose exec driver alembic upgrade head
```


## sensors

- 1-ぴー: EB:EA:8A:94:5C:D8
- 2-そら: C4:43:D5:0d:4D:F4
- 3-じん: FD:6B:1D:D9:15:56
- 4-きな: DC:08:9A:D2:9B:8A
- 5-ゆき: C2:B9:B2:F8:24:12
- 6-リビング: C3:FF:42:9F:D2:0A

## plugs

- 1-ぴー: 10:27:F5:22:07:C9
- 2-そら: AC:84:C6:51:14:91
- 3-じん: 10:27:F5:22:08:E7
- 4-きな: 0C:80:63:04:FD:0B
- 5-ゆき: 10:27:F5:22:08:12

## 実行マシン

### DB･Webサーバ

gn-sv-08

### センサー情報収集

gn-sv-11

### Viewer

gn-cl-05

## 構築

```sh
# Docker
curl -fsSL https://get.docker.com/ | sh
curl -fsSL https://get.docker.com/gpg | sudo apt-key add
sudo curl -L https://github.com/docker/compose/releases/download/v2.5.0/docker-compose-linux-armv7 -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G sudo gretel
sudo usermod -a -G docker gretel
```

```sh
# Python
sudo apt update
sudo apt install -y git make build-essential openssl wget curl llvm \
  libssl-dev libbz2-dev libreadline-dev libsqlite3-dev zlib1g-dev \
  libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

git clone https://github.com/yyuu/pyenv.git ~/.pyenv
git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

cat < EOL >> ~/.bashrc
# pyenv and virtualenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
EOL

cd ~/pi-temp-cm/driver/admin-daemon
pyenv install --list
pyenv install 3.9.9
pyenv virtualenv 3.9.9 admin-daemon
pyenv local admin-daemon
```

```sh
# node npm
curl -fsSL https://deb.nodesource.com/setup_17.x | bash -
sudo apt-get install -y nodejs

# tplink-smarthome-api
sudo npm install -g tplink-smarthome-api
/usr/local/bin/tplink-smarthome-api search
```

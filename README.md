# TempKeeper

令和最新版の小鳥のケージの温度を管理するソリューション！！！


## alembic

```bash
# マイグレーション
docker-compose exec cm-daemon alembic upgrade head

# 新しいリビジョンを作る
docker-compose exec cm-daemon alembic revision -m "revision_name"
```

## Development

```bash
# driver
docker-compose exec cm-daemon python3 /var/driver/main.py
```


## DB破壊

```
docker-compose stop pgsql && docker-compose rm pgsql && docker-compose up -d pgsql
docker-compose exec driver alembic upgrade head
```

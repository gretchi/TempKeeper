# TempKeeper

令和最新版の小鳥のケージの温度を管理するソリューション！！！


## alembic

```bash
# マイグレーション
docker-compose exec driver alembic upgrade head

# 新しいリビジョンを作る
docker-compose exec driver alembic revision -m "revision_name"
```

## Development

```bash
# driver
docker-compose exec driver python3 /var/driver/main.py
```


## DB破壊

```
docker-compose stop pgsql && docker-compose rm pgsql && docker-compose up -d pgsql
docker-compose exec driver alembic upgrade head
```


## sensors

- 1-ぴー: EB:EA:8A:94:5C:D8
- 2-そら: C4:43:D5:0d:4D:F4
- 3-じん: FD:6B:1D:D9:15:56
- 4-きな: DC:08:9A:D2:9B:8A
- 5-ゆき: C2:B9:B2:F8:24:12

## plugs

- 1-ぴー: 10:27:F5:22:07:C9
- 2-そら: AC:84:C6:51:14:91
- 3-じん: 10:27:F5:22:08:E7
- 4-きな: 0C:80:63:04:FD:0B
- 5-ゆき: 10:27:F5:22:08:12

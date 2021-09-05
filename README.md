# RSS2CHANNEL

通过bot发布RSS源消息到telegram频道

RSS to Telegram Channel 
via Telegram bot

# PREPARE

准备

 - 待发布的RSS源，支持url和file path
 - 通过[@BotFather](https://t.me/BotFather)创建Telegram bot,获取`token`
 - 创建你发布消息源的Telegram channel
 - 将创建的Telegram bot设置为频道管理员



 - have RSS source
 - Create Telegram bot,get `token`
 - Telegram channel owner
 - Telegram bot as channel admin



## INSTALL

需要提前安装python包管理器[poetry](https://poetry.eustace.io/docs)

You need to install [poetry](https://poetry.eustace.io/docs) in advance.

```
$ poetry install

```

## USAGE

```
# modify config.yaml

# run
$ poetry run python3  ./main.py 
```

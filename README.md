# RSS2CHANNEL

通过bot发布RSS源消息到telegram频道

RSS to Telegram Channel 
via Telegram bot

# DEMO

[@天府通消息](https://t.me/tianfutong)

# PREPARE

准备

 - 待发布的RSS源，支持url和file path
 - 通过[@BotFather](https://t.me/BotFather)创建Telegram bot,获取`token`
 - 创建你发布消息源的Telegram channel
 - 将创建的Telegram bot设置为频道管理员


## INSTALL

安装

需要提前安装python包管理器[poetry](https://poetry.eustace.io/docs)

```
$ pipenv install

```

## USAGE

使用

```
# modify config.yaml

# run
$ pipenv run python3  ./main.py 
```

## ADVANCED

高级用法

定义自己的send_message function()

https://github.com/Hootrix/RSS2Channel/blob/5719f210958069072b340a901904b9624fb31476/main.py#L19

方法，用于设置发布消息格式。

查看：https://github.com/eternnoir/pyTelegramBotAPI#telebot


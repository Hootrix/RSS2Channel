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

--

 - have RSS source
 - Create Telegram bot,get `token`
 - Telegram channel owner
 - Telegram bot as channel admin



## INSTALL

安装

需要提前安装python包管理器[poetry](https://poetry.eustace.io/docs)

You need to install [poetry](https://poetry.eustace.io/docs) in advance.

```
$ poetry install

```

## USAGE

使用

```
# modify config.yaml

# run
$ poetry run python3  ./main.py 
```

## ADVANCED

高级用法

定义自己的[send_message function()](https://github.com/Hootrix/RSS2Channel/blob/5719f210958069072b340a901904b9624fb31476/main.py#L19)方法，用于设置发布消息格式。
查看：https://github.com/eternnoir/pyTelegramBotAPI#telebot

--

Define your  [send_message The function ()] (https://github.com/Hootrix/RSS2Channel/blob/5719f210958069072b340a901904b9624fb31476/main.py#L19) method, Set the format of a published message.
Look at: https://github.com/eternnoir/pyTelegramBotAPI#telebot

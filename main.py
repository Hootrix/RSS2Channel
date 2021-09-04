from feedparser.exceptions import ThingsNobodyCaresAboutButMe
import telebot,logging,time
import feedparser
import diskcache as dc
import yaml,os

"""
RSS源的Telegram频道消息发布
"""

_current_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{_current_path}/config.yaml') as _f:
  config = yaml.load(_f.read(),Loader = yaml.SafeLoader)

cache = dc.Cache(f'{_current_path}/.tmp')
logging.basicConfig(filename=f"{_current_path}/.log",level=logging.DEBUG  if config['DEBUG']  else logging.ERROR,format="[%(levelname)s][%(name)s]%(asctime)s  %(message)s",datefmt='%Y-%m-%d %H:%M:%S%Z')
logging.root = logging.getLogger('RSS2Channel.main')
bot = telebot.TeleBot(config['bot-token'])

def send_message(cache_key,channel,feed_item):
  """
  发送消息到频道 
  # todo 自定义消息发送操作以及类型
  """
  logging.debug(f'send_message--> {channel} {feed_item}')
  title = feed_item.title if feed_item.title == feed_item.description else '%s\n%s'%(feed_item.title,feed_item.description)
  msg = f'<b>{title}</b>\n\n{feed_item.description}\n\n{feed_item.link}'
  # rel = bot.send_photo(channel,feed_item.guid,msg,parse_mode='HTML')
  rel = bot.send_message(channel,msg,parse_mode='HTML')
  if hasattr(rel,'message_id'):
    logging.debug(f'message_id--> {rel.message_id}')
    #todo 后续操作。。。
    cache.set(cache_key,feed_item)#标记最近发布
    

def track_rss(channel,rss,callback = None):
  """
  消息发布
  
  Keyword Arguments:
      channel 频道id  e.g. @tianfutong
      rss 订阅源 e.g. http://url/feed or /path/rss.xml
      callback 发布消息的回调拦截
  """
  cache_key = '__RSS2CHANNEL_LAST_POST'
  #读取rss
  _feed = feedparser.parse(rss)
  feed = sorted(_feed['items'], key=lambda item: item["updated_parsed"],reverse=True)#按照时间降序
  if callback and callable(callback):
    logging.debug('execute callable: func(feed,bot)')
    callable(feed,bot)
  else:#默认处理
    find_cache = cache.get(cache_key,default=None) #查询上一次发布的信息
    if find_cache:#之前有过发布记录
      # publishing = []
      guids = [i.guid for i in feed]
      if find_cache.guid in guids:#存在之前的发布信息
        index = guids.index(find_cache.guid)
        if index != 0:#不是最新的消息。最新消息未发送
          for i in reversed(feed[:index]):# 从旧到新发布
            logging.debug('find new message:'+i.title)
            send_message(cache_key,channel,i)
            time.sleep(1)
        else:
          logging.debug('no update.')
      else:#不存在之前信息 则发布所有
        for i in reversed(feed):# 从旧到新发布
          if i.updated_parsed >= find_cache.updated_parsed:# 仅仅是时间比那条新的才会发布  避免重复发布（因为rss源有可能会删除其中的消息）
            send_message(cache_key,channel,i)
            time.sleep(1)
    else:# 第一次发布
      cache.set(cache_key,feed[0]) # 下次更新生效
      logging.debug('not found cache,send a new message next time.')


# 机器人消息回复功能
# bot.polling() #none_stop=True 不停止
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	# bot.reply_to(message, '固定消息') #message.text
#   # bot.send_message("@tianfutong",'冬最大范围降雪来袭 四川的雪都下在川西了 ![123](http://tfsmy.chengdu.gov.cn/cms/userfiles/2/_thumbs/images/cms/article/2020/01/1(6).png)') #  
#   # rel = bot.send_photo("@tianfutong",'http://tfsmy.chengdu.gov.cn/cms/userfiles/2/_thumbs/images/cms/article/2020/01/1(6).png','冬最大范围降雪来袭 四川的雪都下在川西了 ! \nhttp://tfsmy.chengdu.gov.cn/cms/share/news?id=c429be8272324dd1aeda202965228f79',parse_mode='HTML')
#   # logging.debug(rel.message_id)
#   pass

if __name__ == "__main__":
  while True:
    track_rss(channel=config['tg-channel'],rss=config['RSS'])
    time.sleep(5) # 检查rss间隔 5秒

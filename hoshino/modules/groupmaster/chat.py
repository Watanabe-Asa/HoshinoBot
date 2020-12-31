import random
import pytz
from nonebot import on_command
from datetime import datetime
import hoshino
from hoshino import R, Service, priv, util

tz = pytz.timezone('Asia/Shanghai')

# basic function for debug, not included in Service('chat')
@on_command('zai?', aliases=('在?', '在？', '在吗', '在么？', '在嘛', '在嘛？'), only_to_me=True)
async def say_hello(session):
    await session.send('はい！私はいつも貴方の側にいますよ！')


sv = Service('chat', visible=False)

@sv.on_fullmatch('沙雕机器人')
async def say_sorry(bot, ev):
    await bot.send(ev, 'ごめんなさい！嘤嘤嘤(〒︿〒)')


@sv.on_fullmatch(('老婆', 'waifu', 'laopo'), only_to_me=True)
async def chat_waifu(bot, ev):
    if not priv.check_priv(ev, priv.SUPERUSER):
        await bot.send(ev, R.img('laopo.jpg').cqcode)
    else:
        await bot.send(ev, 'mua~')


@sv.on_fullmatch('老公', only_to_me=True)
async def chat_laogong(bot, ev):
    await bot.send(ev, '你给我滚！', at_sender=True)


@sv.on_fullmatch('mua', only_to_me=True)
async def chat_mua(bot, ev):
    await bot.send(ev, '笨蛋~', at_sender=True)


@sv.on_fullmatch('来点星奏')
async def seina(bot, ev):
    await bot.send(ev, R.img('星奏.png').cqcode)


@sv.on_fullmatch(('我有个朋友说他好了', '我朋友说他好了', ))
async def ddhaole(bot, ev):
    await bot.send(ev, '那个朋友是不是你弟弟？')


@sv.on_fullmatch('我好了')
async def nihaole(bot, ev):
    await bot.send(ev, '不许好，憋回去！')
    
 
@sv.on_fullmatch(('晚安', '晚安哦', '晚安啦', 'good night'), only_to_me=False)
async def goodnight(bot, ev):
    now_hour=datetime.now(tz).hour
    if now_hour<=4 or now_hour>=21:
        await bot.send(ev, 'おやすみなさい～')
    elif 19<=now_hour<21:
        await bot.send(ev, f'现在才{now_hour}点，这么早就睡了吗？')
    else:
        await bot.send(ev, f'现在才{now_hour}点，还没到晚上啦。')


@sv.on_fullmatch(('早安', '早安哦', '早上好', '早上好啊', '早上好呀', '早', 'good morning'), only_to_me=False)
async def goodmorning(bot, ev):
    now_hour=datetime.now(tz).hour
    if 0<=now_hour<6:
        await bot.send(ev, f'好早，现在才{now_hour}点呢')
    elif 6<=now_hour<10:
        await bot.send(ev, '早上好！今天打算做什么呢？')
    elif 20<=now_hour<24:
        await bot.send(ev, '别闹，准备睡觉啦！')
    else:
        await bot.send(ev, f'{now_hour}点了才起床吗...要注重生活作息哦') 


# ============================================ #


@sv.on_keyword(('确实', '有一说一', 'u1s1', 'yysy'))
async def chat_queshi(bot, ctx):
    if random.random() < 0.05:
        await bot.send(ctx, R.img('确实.jpg').cqcode)


@sv.on_keyword(('会战'))
async def chat_clanba(bot, ctx):
    if random.random() < 0.02:
        await bot.send(ctx, R.img('我的天啊你看看都几度了.jpg').cqcode)


@sv.on_keyword(('内鬼'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.10:
        await bot.send(ctx, R.img('内鬼.png').cqcode)

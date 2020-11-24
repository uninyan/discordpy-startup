from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

boss = [
    {'name': 'ワイバーン'   , 'hp_max': 1000},
    {'name': 'ライライ'     , 'hp_max': 2000},
    {'name': 'オークチーフ' , 'hp_max': 3000},
]
now = {'name': 'aaa'    , 'hp_now': 9}

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

# 発言時に実行されるイベントハンドラを定義
@bot.event
async def on_message(message):
    if message.author.bot: # botを無視(ループ回避)
        return
    if bot.user in message.mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行

# 返信する非同期関数を定義
async def reply(message):
    s = message.content.split()
    reply = s
    if len(s) == 1:
        reply = '現状' + now
    elif s[1] == 'LA':
        now['name']     = boss[0]['name']
        now['hp_now']   = boss[0]['hp_max']
        reply = 'ボス更新' + now
    else:
        reply = f'{message.author.mention} 「' + message.content + '」'
    await message.channel.send(reply) # 返信メッセージを送信

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)

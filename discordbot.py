from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

boss = [
    {'num': 0, 'name': 'ワイバーン'   , 'hp_max': 1000},
    {'num': 1, 'name': 'ライライ'     , 'hp_max': 2000},
    {'num': 2, 'name': 'オークチーフ' , 'hp_max': 3000},
]
now = {'num': 1, 'name': 'aaa'    , 'hp_now': 9}

count = 0

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
    await message.channel.send(reply) # 返信メッセージを送信

    if len(s) == 1:
        reply = now
    elif s[1] == 'LA':
        now['name']     = boss[count]['name']
        now['hp_now']   = boss[count]['hp_max']
        reply = now
        count += 1
        if count == len(boss):
            count = 0
    else:
        reply = f'{message.author.mention} 「' + message.content + '」'
    await message.channel.send(reply) # 返信メッセージを送信

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)

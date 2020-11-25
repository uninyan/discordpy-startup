from discord.ext import commands
import os
import sys
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

boss = [
    {'num': 0, 'name': 'ワイバーン'   , 'hp_max': 1000},
    {'num': 1, 'name': 'ライライ'     , 'hp_max': 2000},
    {'num': 2, 'name': 'オークチーフ' , 'hp_max': 3000},
]
now = {'num': 1, 'name': 'aaa'    , 'hp_now': 9}

yaml_path = ""

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

# 返信する非同期関数を定義
async def reply(message):
    reply = f'{message.author.mention} 「' + message.content + '」'
    await message.channel.send(reply) # 返信メッセージを送信

# 発言時に実行されるイベントハンドラを定義
@bot.event
async def on_message(message):
    if message.author.bot: # botを無視(ループ回避)
        return
    if bot.user in message.mentions:    # メンションされた場合
        message_array = message.content.split()
        if len(message_array) == 1:
            m = reserve_list(message)       # 予約表示
        elif message_array[1] == "解除":
            m = reserve_delete(message)     # 予約解除
        elif message_array[1] == "凸":
            m = attack_declaration(message) # 凸宣言
        elif message_array[1] == "@":
            m = attack_report(message)      # 残HP報告
        elif message_array[1] == "LA":
            m = last_attack_report(message) # LA報告
        elif message_array[1] == 1:
            m = reserve(message)            # 予約
        else:
            m = "ha?"
        await message.channel.send(m) # 返信メッセージを送信
        await reply(message) # 返信する非同期関数を実行

# 予約
async def reserve(message):
    return (sys._getframe().f_code.co_name)

# 予約一覧
async def reserve_list(message):
    return (sys._getframe().f_code.co_name)

# 予約削除
async def reserve_delete(message):
    return (sys._getframe().f_code.co_name)

# 凸宣言
async def attack_declaration(message):
    return (sys._getframe().f_code.co_name)

# 残HP報告
async def attack_report(message):
    return (sys._getframe().f_code.co_name)

# LA報告
async def last_attack_report(message):
    return (sys._getframe().f_code.co_name)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)

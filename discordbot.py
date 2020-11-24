from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# 発言時に実行されるイベントハンドラを定義
@bot.event
async def on_message(message):
    if bot.user in message.mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行

# 返信する非同期関数を定義
async def reply(message):
    if message.content == 'a':
        reply = f'{message.author.mention} aaaaa'
    else:
        reply = f'{message.author.mention} a'

    await message.channel.send(reply) # 返信メッセージを送信

bot.run(token)

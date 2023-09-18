import discord
import asyncio
from discord.ext import commands

Client = discord.Client()
client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
    print("Bot is ready!")


@client.event
async def on_message(message):
    if message.content.startswith("#count"):
        counter = 0
        while counter > -1:
            counter += 1
            await message.channel.send(counter)
            if message.content.startswith("#stopcount"):
                break



client.run("insert token here")



# await asyncio.sleep(num of seconds) (maybe async.sleep(num of seconds))
# the problem is the bot won't stop right away because of discord rate limit




# WORK IN PROGRESS, DEVELOPMENT LIMBO
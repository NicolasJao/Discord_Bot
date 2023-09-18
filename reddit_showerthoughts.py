import praw

import discord
import asyncio
import random as rand
from discord.ext import commands

Client = discord.Client()
client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
    print("Bot is ready!")

reddit = praw.Reddit(client_id='Hmn-1iBQsyZ3HQ', \
                     client_secret='yj6gqrsIuKRO00USs6E51em_AGs', \
                     user_agent='dwnld', \
                     username='DUMB_ACCOUNT_FOR_BOT', \
                     password='redditbot')

subreddit = reddit.subreddit('Showerthoughts')
subredditSearch = subreddit.top(limit=100)

yeet = []

def yeeted():
    bruh = rand.randint(0, 99)
    return bruh

for submission in subredditSearch:
    yeet.append(submission.title + "\n" + submission.selftext)


@client.event
async def on_message(message):
    if message.content.startswith("#showerthought"):
        cool = yeet[yeeted()]
        await message.channel.send(cool)

client.run("insert token here")

# this takes the top 100 reddit posts of r/Showerthoughts and gives you a random one


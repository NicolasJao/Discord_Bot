import discord
import asyncio
from discord.ext import commands
from PIL import Image
from io import BytesIO

Client = discord.Client()
client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
    print("Bot is ready!")


client = commands.Bot(command_prefix = "#")

@client.command()
async def santahat(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    santa_hat = Image.open("/Users/nicojao/Documents/santa_hat.png")

    asset = ctx.author.avatar_url_as(size = 256)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    santa_hat = santa_hat.resize((150,100))

    pfp.paste(santa_hat, (75,10))

    pfp.save("profile.png")

    await ctx.send(file = discord.File("profile.png"))

client.run("insert token here")

# My attempt to put a santa hat on your profile picture and send it when requested

# Debugging Steps:
# if you get "Cannot connect to host discordapp.com:443" go to Applications, Python 3.8
# and double click "Install Certificates"
# If you get deny_new, re-install discord.py with "python3 -m pip install -U discord.py"

# # Transparency
# newImage = []
# for item in image.getdata():
#    if item[: 3] == (255, 255, 255):
#    newImage.append((255, 255, 255, 0))
# else :
#    newImage.append(item)
#
# image.putdata(newImage)
# image.save('output.png')

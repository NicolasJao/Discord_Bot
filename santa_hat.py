import discord
import asyncio
from discord.ext import commands
import PIL
from PIL import Image
from io import BytesIO
import cv2
import numpy

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

    santa_hat = cv2.imread("/Users/nicojao/Documents/santa_hat.png", -1)

    asset = ctx.author.avatar_url_as(size = 256)
    data = BytesIO(await asset.read())
    pfp = PIL.Image.open(data)
    pfp_opencv = numpy.array(pfp)
    pfp_opencv = cv2.cvtColor(pfp_opencv, cv2.COLOR_RGB2BGR)

    new_size = (150, 100)
    santa_hat_resized = cv2.resize(santa_hat, new_size, interpolation=cv2.INTER_LINEAR)

    x_offset = 70
    y_offset = 0
    y1, y2 = y_offset, y_offset + santa_hat_resized.shape[0]
    x1, x2 = x_offset, x_offset + santa_hat_resized.shape[1]

    alpha_paste = santa_hat_resized[:, :, 3] / 255.0
    alpha_background = 1.0 - alpha_paste

    for c in range(0, 3):
        pfp_opencv[y1:y2, x1:x2, c] = (alpha_paste * santa_hat_resized[:, :, c] + alpha_background * pfp_opencv[y1:y2, x1:x2, c])
    pfp_opencv = cv2.cvtColor(pfp_opencv, cv2.COLOR_BGR2RGB)

    final_img = Image.fromarray(pfp_opencv)
    final_img.save("profile.png")

    await ctx.send(file = discord.File("profile.png"))

client.run("")

# Using both PIL and openCV, this puts a santa hat on your profile picture and sends it back on discord
# after using the #santahat command. Merry Christmas!

# Debugging Steps:
# if you get "Cannot connect to host discordapp.com:443" go to Applications, Python 3.8
# and double click "Install Certificates"
# If you get deny_new, re-install discord.py with "python3 -m pip install -U discord.py"

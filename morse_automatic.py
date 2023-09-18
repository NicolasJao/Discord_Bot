import discord
import asyncio
from discord.ext import commands

Client = discord.Client()
client = commands.Bot(command_prefix = "!")


def encode_morse(message):
    dictionary = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
        ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
        '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }
    output = ""
    firstTime = True
    for char in message.upper():
        if firstTime:
            output += (dictionary[char])
            firstTime = False
        else:
            output += " " + (dictionary[char])
    return output


def translate_morse(message):
    dictionary = {
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
        '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
        '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
        '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
        '-.--': 'y', '--..': 'z', ' ': ' ', '-----': '0',
        '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
        '-....': '6', '--...': '7', '---..': '8', '----.': '9',
        '.-...': '&', ".----.": "'", '.--.-.': '@', '-.--.-': ')', '-.--.': '(',
        '---...': ':', '--..--': ',', '-...-': '=', '-.-.--': '!', '.-.-.-': '.',
        '-....-': '-', '.-.-.': '+', '.-..-.': '""', '..--..': '?', '-..-.': '/'
    }
    charlist = message.split()
    output = ""
    firstTime = True
    for item in charlist:
        if firstTime:
            output += (dictionary[item])
            firstTime = False
        else:
            output += " " + (dictionary[item])
    return output


def check_if_morse(thing):
    for char in thing:
        if char == " " or char == "." or char == "-":
            continue
        else:
            return False
    return True


@client.event
async def on_ready():
    print("Bot is ready!")


@client.event
async def on_message(message):
    if message.author.id == 769418371162701875:
        pass
    else:
        if check_if_morse(message.content):
            try:
                response = translate_morse(message.content)
                await message.channel.send(response)
            except:
                pass
        elif not check_if_morse(message.content):
            try:
                response = encode_morse(message.content)
                await message.channel.send(response)
            except:
                pass


client.run("insert token here")

# translates from english to morse code and back

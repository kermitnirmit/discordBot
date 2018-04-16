import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "")
eyyCounter = 0
lmaoCounter = 0
lmfaoCounter = 0
sameCounter = 0
@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    if message.content.lower().find("mood") > -1:
        await client.send_message(message.channel, "Here's a :cookie:")
    if message.content.lower().find("m o o d") > -1:
        await client.send_message(message.channel, "Here's a :cookie:")
    if message.content.lower().find("eyy") > -1:
        global eyyCounter
        eyyCounter = eyyCounter + 1
        toReturn = str(eyyCounter)
        await client.send_message(message.channel, toReturn)
    if message.content.lower().find("lmao") > -1:
        global lmaoCounter
        lmaoCounter = lmaoCounter + 1
        toReturn = str(lmaoCounter)
        await client.send_message(message.channel, toReturn)
    if message.content.lower().find("lmfao") > -1:
        global lmfaoCounter
        lmfaoCounter = lmfaoCounter + 1
        toReturn = str(lmfaoCounter)
        await client.send_message(message.channel, toReturn)
    if message.content == "yuzu":
        await client.send_message(message.channel, "You meant Nathan Chen right?")
    if message.content.lower().find("same") == 0:
        global sameCounter
        sameCounter = sameCounter + 1
        toReturn = str(sameCounter)
        await client.send_message(message.channel, toReturn)
    if message.content.lower().find("nermit") > -1:
        await client.send_message(message.channel, "It's spelled Nirmit")
    if message.content.lower().find("jkl") > -1:
        await client.send_message(message.channel, "nice keyspam")
    if message.content.lower().find("im dying") > -1:
        await client.send_message(message.channel, "that is suboptimal")
    if message.content.lower().find("im dead") > -1:
        await client.send_message(message.channel, "lol rip")
    if message.content.lower().find("lm") > -1:
        await client.send_message(message.channel, "stop it")
    if message.content.lower().find("fuck you nirmit") > -1:
        await client.send_message(message.channel, "classic")
    if message.content.lower().find("nathan chen") > -1:
        await client.send_message(message.channel, "Correct. You deserve a :cookie:")

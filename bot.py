import discord
import string
from dotenv import load_dotenv
import os
import random
from discord.ext import commands
from pymongo import MongoClient

bot = commands.Bot(command_prefix="./")
client = MongoClient("mongodb://localhost:27017/")
coll = client.bitly.database
load_dotenv(verbose=True)

TOKEN = os.getenv("TOKEN")


@bot.event
async def on_ready():
    print(f"{str(bot.user)} 준비 완료.")


@bot.command(name="추가")
async def Add(ctx, link: str):
    result = str()
    for i in range(10):
        result += random.choice(string.ascii_letters)
    data = {"_id": result, "query": link}
    coll.insert_one(data)
    await ctx.send(f"정상적으로 처리 되었습니다. Url은 http://test.sonicbot.club/{result}")


bot.run(TOKEN)
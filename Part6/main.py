import discord
from discord.ext import commands
#pip install rwquests
import requests

@bot.command()
async def trans(ctx, *, msg):
    trans_now = await ctx.send("日本語から英語に翻訳中です...")
    api_key = "ffaa0bf1-9daa-3c71-efa9-8061590ba037:fx"
    params = {
                "auth_key": api_key,
                "text": str(msg),
                "source_lang": "JA",
                "target_lang": "EN"
            }

    request = requests.post("https://api-free.deepl.com/v2/translate", data=params)
    result = request.json()
    await trans_now.edit(content="JA → EN\n" + result["translations"][0]["text"])

bot.run(Token)
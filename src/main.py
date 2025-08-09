import asyncio
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from articles_functions import select_article

load_dotenv()

discord_token = os.environ['DISCORD_TOKEN']
channel_id = int(os.environ['CHANNEL_ID'])

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

async def send_message():
    await bot.login(discord_token)
    channel = bot.get_channel(channel_id)

    if channel is None:
        channel = await bot.fetch_channel(channel_id)

    selected_article = select_article()

    max_description_len = 1500
    description = selected_article[1]
    if len(description) > max_description_len:
        description = description[:max_description_len] + '...'
    message = (
        f"**Bora ler uma matéria para pensar um pouco fora da caixinha e ir além do código? 🤔**\n\n"
        f"O texto de hoje é: **{selected_article[0]}**\n\n"
        f"*{description}*\n\n"
        f"🔗 Para ler o texto completo, clique [aqui]({selected_article[2]})\n\n"
        f"Espero que você goste da sugestão! 😄"
    )

    await channel.send(message)
    await bot.close()

asyncio.run(send_message())

import os
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv

load_dotenv()

response = requests.get("https://www.technologyreview.com/topic/artificial-intelligence/feed")
soup = BeautifulSoup(response.text, "xml")
articles = soup.find_all("item")

discord_token = os.environ['DISCORD_TOKEN']
channel_id = int(os.environ['CHANNEL_ID'])

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

def load_sent_links():
    try:
        with open("sent_links.txt", "r") as f:
            return set(f.read().splitlines())
    except FileNotFoundError:
        return set()

def save_sent_link(link):
    with open("sent_links.txt", "a") as f:
        f.write(link + "\n")

async def main():
    await bot.login(discord_token)
    channel = bot.get_channel(channel_id)
    if channel is None:
        channel = await bot.fetch_channel(channel_id)
    
    sent_links = load_sent_links()
    for article in articles:
        titulo_artigo = article.find("title").text
        descricao_artigo = article.find("description").text
        descricao_artigo = BeautifulSoup(descricao_artigo, "html.parser").text
        link_artigo = article.find("link").text

        if link_artigo in sent_links:
            continue
        
        job_message = (
            f"**Bora ler uma matéria para pensar um pouco fora da caixinha e ir além do código? 🤔**\n\n"
            f"O texto de hoje é: **{titulo_artigo}**\n\n"
            f"*{descricao_artigo}*\n\n"
            f"🔗 Para ler o texto completo, clique [aqui]({link_artigo})\n\n"
            f"Espero que você tenha gostado da sugestão de hoje! 😄"
        )
        await channel.send(job_message)
        save_sent_link(link_artigo)
        break
    await bot.close()

import asyncio
asyncio.run(main())

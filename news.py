from bs4 import BeautifulSoup
import requests
import asyncio
import os
import discord 
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

response = requests.get("https://www.technologyreview.com/topic/artificial-intelligence/feed")
list_articles = response.text
soup = BeautifulSoup(list_articles, "xml")
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

async def send_scheduled_message():
    await bot.wait_until_ready()
    channel = bot.get_channel(channel_id)

    while not bot.is_closed():
        sent_links = load_sent_links()

        for article in articles:
            titulo_artigo = article.find("title").text
            descricao_artigo = article.find("description").text
            descricao_artigo = BeautifulSoup(descricao_artigo, "html.parser").text
            link_artigo = article.find("link").text

            if link_artigo in sent_links:
                print(f"[{datetime.now()}] Já enviou esse artigo, pulando...")
                continue

            job_message = (
                f"**Bora ler uma matéria para pensar um pouco fora da caixinha e ir além do código? 🤔**\n\n"
                f"O texto de hoje é: **{titulo_artigo}**\n\n"
                f"*{descricao_artigo}*\n\n"
                f"🔗 Para ler o texto completo, clique [aqui]({link_artigo})\n\n"
                f"Espero que você tenha gostado da sugestão de hoje! 😄"
            )

            if channel:
                await channel.send(job_message)
                save_sent_link(link_artigo)
                break 

        await asyncio.sleep(86400)  
                
@bot.event
async def on_ready():
    bot.loop.create_task(send_scheduled_message())

def main():
    bot.run(discord_token)

if __name__ == "__main__":
    main()

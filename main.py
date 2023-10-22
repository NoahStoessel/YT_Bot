import discord
from discord import app_commands
from discord.ext import commands
#from download import download_video
bot = commands.Bot(command_prefix="!", intents = discord.Intents.none())
from pytube import YouTube
import os
import time
from token_discord import TOKEN

def download_video(url, nr):
    yt = YouTube(url=url)
    video = yt.streams.get_highest_resolution()
    print(f"Downloadign {url} as {nr}")
    video.download(filename=nr)
    print("Waiting 1 seconds!")
    print("Removing!")
    os.remove(nr)

@bot.event
async def on_ready():
    print("Bot up!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except:
        print("Something went wrong")
@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention} !", ephemeral=True)
    print("Command ran!")
@bot.tree.command(name="download")
@app_commands.describe(link = "youtube video link")
async def download(interaction: discord.Interaction, link: str):
    await interaction.response.defer()
    download_video(link, str(interaction.user.id) + str(interaction.created_at.second))
    await interaction.edit_original_response(content=f"Link is: {link}")
bot.run(TOKEN)
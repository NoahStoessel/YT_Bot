import discord
from discord import app_commands
from discord.ext import commands
#from download import download_video
bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())
from pytube import YouTube
import os
import time
from token_discord import TOKEN

def download_video(url):
    yt = YouTube(url=url)
    video = yt.streams.get_highest_resolution()
    print("Filename: ")
    print(str(yt.streams[0].title) + ".mp4")
    filename = str(yt.streams[0].title) + ".mp4"
    video.download()
    print("Waiting 1 seconds!")
    #time.sleep(1)
    print("Removing!")
    os.remove(filename)

@bot.event
async def on_ready():
    print("Bot up!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except:
        print(e)
@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention} !", ephemeral=True)
    print("Command ran!")
@bot.tree.command(name="download")
@app_commands.describe(link = "youtube video link")
async def download(interaction: discord.Interaction, link: str):
    await interaction.response.send_message(f"Link is: {link}", ephemeral=True)
    download_video(link)
bot.run(TOKEN)
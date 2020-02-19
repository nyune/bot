import discord
import openpyxl
import requests
import asyncio
from json import loads


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("넨글봇")
    await client.change_presence(status=discord.Status.online, activity=game)
    twich = "Nenyes0426"
    name = "넨글"
    channel = client.get_channel(679713180293136391)
    a = 0
    while True:
        headers = {'Client-ID': 'ebqn2vp139wshwnf6kjztcqtpop078'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twich, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                await channel.send(name + "님이 방송중입니다.https://www.twitch.tv/nenyes0426/")
                a = 1
        except:
            a = 0
        await asyncio.sleep(3)

client.run('Njc5NTgxNDYyNTI5NzAzOTk3.Xk1Ydw.Huu3wg0IYVpIpodb9iFe4ku4bmU')
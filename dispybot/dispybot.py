import discord, requests, re, os, json, sys, traceback, ffmpeg, time, random
from termcolor import colored as c
from getdata import getapitoken, getsong
from discord.ext import commands
prefixes = ["!","£","$","%","^","&","*","tempo"]
intents = discord.Intents.all()
try:
    with open("config.json", "r") as f:
        config = json.load(f)
except FileNotFoundError:
    print(c("[!] Config File Not Found","red"))
    sys.exit()
try:
    token = config["token"]
except KeyError:
    print(c("[!] Token Not Found","red"))



tempowave = commands.Bot(command_prefix=prefixes,intents=intents,status=discord.Status.idle)
tempowave.remove_command("help")
@tempowave.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice_client = await channel.connect()
        await ctx.send(f"Joined {channel.name}!")
    else:
        await ctx.send("Not in a voice channel.")

@tempowave.command()
async def leave(ctx):
    voice_client = ctx.voice_client
    if voice_client:
        await voice_client.disconnect()
        await ctx.send("Left the voice channel.")
    else:
        await ctx.send("Not in a voice channel.")
@tempowave.command()
async def play(ctx, url):
    voice_client = ctx.voice_client
    if voice_client:
        if voice_client.is_playing():
            await ctx.send("I'm already playing audio.")
            return
        try:
            await ctx.send("loading please wait.")
            rand = random.randint(1, 10000000000000000000000000)
            os.system(f"spotdl {url}")
            os.system(f"mv file.mp3 spotdlsong/downloaded/{rand}.mp3")
            fpath = f"spotdlsong/downloaded/{rand}.mp3"
            voice_client.stop()
            voice_client.play(discord.FFmpegPCMAudio(fpath))
            r = getapitoken()
            track_id = url.split('/')[-1].split('?')[0]
            s = getsong(r, track_id)
            author = s[0]
            title = s[1] 
            embed = discord.Embed(title="Tempowave Media Player",url="https://tempowave.xyz",description=f"Song Playing.\n\nTtitle: {title}\nAuthor: {author}",colour=0x00b0f4)
            await ctx.reply(embed=embed)
        except FileNotFoundError:
            await ctx.send(f"File not found: {fpath}")
            print("failed")
    else:
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            voice_client = await channel.connect()
@tempowave.command()
async def stop(ctx):
    voice_client = ctx.voice_client
    if voice_client:
        await voice_client.disconnect()
        await ctx.send("Stopped playing.")
    else:
        await ctx.send("Not Playing anything.")


@tempowave.command()
async def exit(ctx):
    sys.exit()
@tempowave.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(tempowave.latency * 1000)}ms")
@tempowave.command()
async def help(ctx):
    await ctx.send(f"**{tempowave.user.name} Commands**\n\n`!ping` - Pong!\n`!say` - Say something through the bot\n`!exit` - Exit the Bot\n`!upload 'url'`- Upload a song to the server\n\n")
@tempowave.command()
async def say(ctx,*,message):
    await ctx.send(message)
@tempowave.command()
async def upload(ctx,url):
    if url == None:
        await ctx.send("Error. No URL Provided.")
        pass
    if re.search(r"https://open.spotify.com",url):
        if re.search("playlist",url):
            await ctx.send("Error. Cannot Upload Playlist.")
            pass
        else:
            member = ctx.author
            embed = discord.Embed(title="TempoWave",description="Soon your song will be uploaded on our systems please wait...",colour=0x00b0f4)
            embed.set_footer(text="TempoWave Upload System")    
            await ctx.send(embed=embed)
            os.chdir("supload/songs")
            os.system(f"spotdl {url}")
            os.chdir("/workspaces/imgrepo")
            os.system("python3 getsong.py")
            r = getapitoken()
            track_id = url.split('/')[-1].split('?')[0]
            s = getsong(r, track_id)
            author = s[0]
            title = s[1] 
            newsong = discord.Embed(title="TempoWave",description=f"\nTitle: {title}\nArtist: {author}",colour=0x00b0f4)
            newsong.set_footer(text=f"TempoWave Upload System - Uploaded By {member.name}")
            ch = tempowave.get_channel(1159760219178537012)
            await ch.send(content=f"<@&1159763810551349309>",embed=newsong)
            os.system("clear")
    else:
        member = ctx.author
        embed = discord.Embed(title="TempoWave",description="Song URL did not contain a spotify link...",colour=0x00b0f4)
        embed.set_footer(text="TempoWave Upload System")   
        await ctx.send(content=f"<@{member.id}>",embed=embed)
@tempowave.command()
async def embed(ctx):
    embed = discord.Embed(title="TempoWave Support Rules",
                      description="1. Choose the Correct Category: Select the appropriate ticket category or channel based on the nature of your issue or request. This helps route your ticket to the right support team.\n\n2. Be Concise: Keep your ticket concise and to the point. Avoid unnecessary backstory or unrelated information.\n\n3. Use Proper Formatting: Use proper formatting when necessary to make your ticket easier to read. For example, use bullet points or numbered lists for multiple issues or steps.\n\n4, Be Patient: Support staff may take some time to respond, especially during busy periods. Be patient and avoid spamming the channel with repeated messages.\n\n5. Follow Server Rules: Adhere to the server's general rules and guidelines while interacting in the ticketing system.",
                      colour=0x00b0f4)

    embed.set_footer(text="TempoWave LLC")
    await ctx.send(embed=embed)
@tempowave.event
async def on_ready():
    print("bot is ready")
    await tempowave.change_presence(status=discord.Status.dnd, activity=discord.Game("https://tempowave.xyx"))
try:
    tempowave.run(token)
except discord.LoginFailure as e:
    print(e)
    print(c(f"[!] Login Failed [!]","red"))
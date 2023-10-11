import sys
sys.exit()

@tempowave.command()
async def help(ctx):
    await ctx.send("**TempoWave Commands**\n\n`!ping` - Pong!\n`!say` - Say something through the bot\n`!exit` - Exit the Bot\n`!upload 'url'`- Upload a song to the server\n\n **Music Commands**\n`!join` - Join your voice channel\n`!leave` - leave the voice channel\n`!play` - Play a song\n`!stop` - Stops the currently playing song.\n`!play {url}` - plays the song in the voice channel")

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


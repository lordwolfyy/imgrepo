import discord, requests, re, os, json, sys, traceback
from termcolor import colored as c
from discord import app_commands



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

gid = int(input(c("[!] Guild ID: ","red")))

guild = discord.Object(gid)













class MyClient(discord.Client):
    def __init__(self) -> None:
        intents = discord.Intents.all()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(c(f'Logged in as {self.user} (ID: {self.user.id})',"green"))
        print('------')

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=guild)
class linkview(discord.ui.View):
    def __init__(self):
        super().__init__()
        url = "https://tempowave.xyz"
        self.add_item(discord.ui.Button(label='Site', url=url))

class upgui(discord.ui.Modal, title='Upload'):
    link = discord.ui.TextInput(
        label='Song Url',
        style=discord.TextStyle.long,
        placeholder='https://spotify.com/',
        required=True,
        max_length=300,
    )

    async def on_submit(self, interaction: discord.Interaction):
            if re.match(r"https://spotify.com", self.link.value):
                embed = discord.Embed(title="TempoManagment",url="https://tempowave.xyz",description="hey. your song should be uploading soon.",colour=0x4eda1b)
                embed.set_footer(text="TempoWave Upload System")
                await interaction.response.send_message(embed=embed,ephemeral=True)
                os.chdir("supload/songs")
                os.system(f"spotdl {self.link.value}")
                os.chdir("/workspaces/imgrepo")
                os.system("python3 getsong.py")
    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)
        traceback.print_exception(type(error), error, error.__traceback__)


client = MyClient()


@client.tree.command(guild=guild, description="Submit feedback")
async def feedback(interaction: discord.Interaction):
    await interaction.response.send_modal(upgui())
@client.tree.command(guild=guild, description="Upload a song")
async def upload(interaction: discord.Interaction):
    await interaction.response.send_modal(upgui())
try:
    client.run(token)
except discord.LoginFailure as e:
    print(e)
    print(c(f"[!] Login Failed [!]","red"))
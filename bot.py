import discord
import IBMWatson
client = discord.Client()

@client.event
async def on_ready():
	print("MoodUp is ready!")
	await client.change_presence(game=discord.Game(name="Checking your mood"))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	await client.send_message(message.channel, get_current_mood(message.content))

client.run('NTA4MzM4NjA4NDk1NjU2OTcw.Dr9zAg.gfXUpyELkCiycAt8pSwd66cOmT4')
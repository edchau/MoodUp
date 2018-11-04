import discord
import IBMWatson as ibmw
import ImageSearch
import Clarifai

client = discord.Client()

### Test
# print(ibmw.auto_response(''))

# tested
def is_sad(text):
	for tone in ibmw.get_document_tones(ibmw.get_tone(text)):
		if tone == 'sadness':
			return True
	return False


@client.event
async def on_ready():
	print("MoodUp is ready!")
	await client.change_presence(game=discord.Game(name="Checking your mood"))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if(message.attachments):
		print("attached url: ", message.attachments[0]['url'])
		print("predictions: ", Clarifai.predict_image(message.attachments[0]['url'])['outputs'][0])
		await client.send_message(message.channel, Clarifai.predict_image(message.attachments[0]['url'])['outputs'][0])
	if(message.embeds):
		print("embedded url: ", message.embeds[0]['url'])
		print("predictions: ", Clarifai.predict_image(message.embeds[0]['url'])['outputs'][0])
		await client.send_message(message.channel, Clarifai.predict_image(message.embeds[0]['url'])['outputs'][0])

	await client.send_message(message.channel, ibmw.auto_response(message.content))

	if is_sad(message.content):
		e = discord.Embed(description='cheer up!')
		e.set_image(url=ImageSearch.search_image_get_url('cute animal'))
		await client.send_message(message.channel, embed=e)

client.run('NTA4MzM4NjA4NDk1NjU2OTcw.Dr9zAg.gfXUpyELkCiycAt8pSwd66cOmT4')
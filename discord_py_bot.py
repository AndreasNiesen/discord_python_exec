import sys
import discord
import datetime
from time import sleep
from io import StringIO

#-----------------------------------------------------------------------------
bot_id = '' 		#string; your bot string thingy - if you created your discord bot, you know whats gotta go here
allowed_ids = []	#int; your own/trusted dicord user ids
#-----------------------------------------------------------------------------

client = discord.Client()

def com_exec(com = ""):
	cout = StringIO()		#\
	old_out = sys.stdout	# > Save std out to var; to return/send back as discord msg
	sys.stdout = cout		#/

	try:
		exec(com)
	except:
		print(' '.join(str(stuff) for stuff in sys.exc_info()))
	res = cout.getvalue()
	
	sys.stdout = old_out	# reset std out
	cout.close()
	return(res)

@client.event
async def on_ready():
	print(f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M")} - Bot "{client.user.name}" with ID "{client.user.id} is ready!"\r\n')

@client.event
async def on_message(message):
	if message.channel.type == discord.ChannelType.private:		#only accepts private messages - remove to read every message (in a group)
		if message.author.id in allowed_ids:					#huge ass security issue if everyone were allowed to use this, limit to super trustworthy people
			print(f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M")} - {message.content}')	#write to file to keep as log
			if message.content.startswith('!python\n'):
				com = '\n'.join(buff for buff in message.content.split('\n')[1:])
				res = com_exec(com)
				print(res)
				await message.channel.send(res)
			elif message.content.startswith('!exit'):
				await message.channel.send('Bye!')
				await client.logout()
	sleep(1)

if __name__ == '__main__':
	client.run(bot_id)
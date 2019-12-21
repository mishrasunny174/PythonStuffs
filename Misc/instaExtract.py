import json

conversations = json.loads(open("messages.json","r").read())

for convo in conversations:
	filename = convo['participants'][0] + convo['participants'][1]+'.txt'
	# print(convo)
	with open(filename, 'w') as file:
		for messages in convo['conversation'][::-1]:
			try:	
				file.write(messages["created_at"]+":"+messages['sender']+":"+messages["text"]+"\n")
			except KeyError:
				print(messages)
			except TypeError:
				print(messages)
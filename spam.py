from telethon.sync import TelegramClient, events

##with love from hduwiz  , TG : godlxss <3
print()
hashtg = input("hash : ")
idtg = int(input("id : "))
px = int(input("how much : "))
per = input("id chela: ")
mes = input("text : ")

api_id = idtg 
api_hash = hashtg

with TelegramClient('proxy', api_id, api_hash) as client:
	for i in range(px):
		client.send_message(per, mes)
		client.send_message(per, mes)
		client.send_message(per, mes)
		client.send_message(per, mes)
		client.send_message(per, mes)
		client.send_message(per, mes)
		client.send_message(per, mes)

from telethon.sync import TelegramClient, events

##with love from hduwiz  , TG : godlxss <3
print("\033[1;32m with love from hduwiz<3  \n")
print("\033[1;0m\n")

hashtg = input("hash : ")
idtg = int(input("id : "))
px = int(input("how much : "))
per = input("username : ")
mes = input("text : ")

api_id = idtg 
api_hash = hashtg

print("Thank You! , Glory to Ukraine! UA")

with TelegramClient('proxy', api_id, api_hash) as client:
	for i in range(px):
		client.send_message(per, mes)
		client.send_message(per, mes)
		client.send_message(per, mes)
		client.send_message(per, mes)
		client.send_message(per, mes)
		client.send_message(per, mes)
		client.send_message(per, mes)

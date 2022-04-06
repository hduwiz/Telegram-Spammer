from telethon.sync import TelegramClient, events

##with love from hduwiz  , TG : godlxss <3
print("\033[1;32m with love from hduwiz<3  \n")
print("\033[1;0m\n")

hashtg = input("hash : ")
idtg = int(input("id : "))
px = int(input("how much : "))
per = input("username : ")
mes = input("text : ")
mes1 = input("text 2 : ")

api_id = idtg 
api_hash = hashtg
print("\033[1;44m Thank You! , \n \033[1;43m Glory of Ukraine! \n")
print("\033[1;0m\n")
with TelegramClient('proxy', api_id, api_hash) as client:
	for i in range(px):
		client.send_message(per, mes)
		client.send_message(per, mes1)
		client.send_message(per, mes)
		client.send_message(per, mes1)
		client.send_message(per, mes)
		client.send_message(per, mes1)
		client.send_message(per, mes)
		client.send_message(per, mes1)
		client.send_message(per, mes)
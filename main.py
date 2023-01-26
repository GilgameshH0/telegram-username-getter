from telethon import TelegramClient, sync

# брать с сайта телеграмма https://my.telegram.org/auth
api_id = ''
api_hash = ''
client = TelegramClient('mirror', api_id, api_hash)

client.start()

#Id чата из которого брать юзернеймы
participants = client.get_participants(-1111111111111, aggressive=False)
for p in participants:
    print(p.username)


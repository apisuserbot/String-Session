# Copyleft (c) 2020 Mr.Miss, All wrongs reserved.
#
# Redistribution and use in source with or
# without modufication, are permitted.


import time
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from pyrogram import Client

select = " "

docs = """Generate your Telegram String Session

P -->> Pyrogram [https://docs.pyrogram.org]
T -->> Telethon [https://docs.telethon.dev]
"""

tutor = """
~ Buka my.telegram.org
~ Masukan API KEY DAN API HASH disini
~ Lalu klik enter
~ Sampai string session selesai
~ Check pesan tersimpan hasil dari STRING_SESSION
"""

template = """
Grup Support : @UserbotTelegramSupport 
            
<code>STRING_SESSION</code> : <code>{}</code>

⚠️ <b>Gunakan String Session dengan hati hati karena kalau ada masalah kami tidak bertanggung jawab</b>"""


print(docs)

while select != ("p", "t"):
    select = input("Pencet t jika ingin deploy King-Ubot < p / t > : ").lower()
    if select == "t":
        print("""\nTelethon selected\nRunning script...""")
        time.sleep(1)
        print(tutor)
        API_KEY = int(input("MASUKAN API KEY : "))
        API_HASH = input("MASUKAN API HASH : ")

        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            session_string = client.session.save()
            saved_messages_template = "#TelethonSession" + template.format(session_string)
            print("\nMengirim String Session...\n")
            client.send_message("me", saved_messages_template, parse_mode="html")
            time.sleep(1)
            print("STRING_SESSION berhasil cek di pesan tersimpan mu")
        break

    elif select == "p":
        print("""\nPyrogram selected.\nRunning script...""")
        time.sleep(1)
        print(tutor)
        with Client(
        "UserBot", 
        api_id=int(input("MASUKAN API KEY : ")),
        api_hash=input("MASUKAN API HASH : ")) as pyrogram:
            saved_messages_template = "#PyrogramSession" + template.format(pyrogram.export_session_string())
            print("\nMengirim String Session...\n")           
            pyrogram.send_message("me", saved_messages_template, parse_mode="html")
            time.sleep(1) 
            print("STRING_SESSION berhasil cek di pesan tersimpanmu")
        break
    
    else:
        print("\nPilih t untuk Telethon p untuk Pyrogram\n")
        time.sleep(1.5)

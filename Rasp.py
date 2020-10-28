#sintax: [canale prendere] [canale mettere] [tempo tra le aggiunte]

from telethon import functions
import asyncio
from userbot.utils import admin_cmd, sudo_cmd

@bot.on(admin_cmd(outgoing=True, pattern="rasp ?(.*)"))
async def cmd_list(event):
    result = event.pattern_match.group(1).split(" ")
    chat = result[0]
    try:
        uno = result[0]
        due = result[1]
        tre = result[2]
    except IndexError:
        event.reply("Usage: .rasp [gruppo da cui prendere i membri] [gruppo a cui mettere i membri] [intervallo tra un utente e un altro]")
    async for x in event.client.iter_participants(chat, 50000):
        user_id = x.id
        if not event.is_channel and event.is_group:
            try:
                await borg(
                    functions.messages.AddChatUserRequest(
                        chat_id=result[1], user_id=user_id, fwd_limit=1000000
                    )
                )
            except Exception as e:
                await event.reply(str(e))
        else:
            try:
                await borg(
                    functions.channels.InviteToChannelRequest(
                        channel=result[1], users=[user_id]
                        )
                    )
            except Exception as e:
                await event.reply(str(e))
        asyncio.sleep(time)
        

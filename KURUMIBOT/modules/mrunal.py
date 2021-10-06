from .. import Mrunal
from telethon import events, Button

@Mrunal.on(events.NewMessage(incoming=True, pattern="/mrunal"))
async def start(event):
    await event.reply("**Hello!**")

""" `.Ping' to getyour ping"""

from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd


@borg.on(admin_cmd("Ping"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("P I N G")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("`P I N G`\n`{}ms`".format(ms))

""".on cmd to see if your userbot is ALIVE or Dead"""

import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd
import uniborg
from os import remove
from platform import python_version, uname
from shutil import which
from telethon import version

from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE

from shutil import which
from os import remove
from telethon import version

from platform import python_version, uname
from sample_config import Config


# ================= CONSTANT =================
DEFAULTUSER = Config.ALIVE_NAME if Config.ALIVE_NAME else uname().node
# ============================================


# @register(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd("on"))
async def amireallyalive(on):
    """ For .on command, check if the bot is running.  """
    await on.edit(
                     "        Welcome\n"
                     " \n"
                     "──────────────────── \n"
                     f"Telethon version: {version.__version__} \n"
                     f"Python: {python_version()} \n"
                     f"──────────────────── \n"
                     f"User: {DEFAULTUSER} \n"
                     " \n"
                     f"Creator: @Mayur_Karaniya \n"
                     " \n"
                     f"Owner: `3Cube TeKnoways` \n"
                     " \n"
                     f"Website: https://www.facebook.com/Teknoways \n"
                     " \n"
                     f"Userbot: testuserbot \n"
                     "`i can't die`")    

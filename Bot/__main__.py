import sys

import userbot
from userbot import BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import legend
from .start import killer
from .utils import (
    add_bot_to_logger_group,
    hekp,
    install_externalrepo,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("userbot")

print(userbot.__copyright__)
print("Licensed under the terms of the " + userbot.__license__)

cmdhr = Config.HANDLER


try:
    LOGS.info("Starting Userbot")
    legend.loop.run_until_complete(setup_bot())
    LOGS.info("TG Bot Startup Completed")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()


async def startup_process():
    try:
        await verifyLoggerGroup()
        await load_plugins("plugins")
        await load_plugins("assistant")
        await externalrepo()
        await killer()
        print("----------------")
        print("Starting Bot Mode!")
        print("⚜ LegendBot Has Been Deployed Successfully ⚜")
        print("OWNER - @LegendBoy_XD")
        print("Group - @Legend_Userbot")
        print("----------------")
        await verifyLoggerGroup()
        await add_bot_to_logger_group(BOTLOG_CHATID)
        if PM_LOGGER_GROUP_ID != -100:
            await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
        await startupmessage()
        await hekp()
    except Exception as e:
        LOGS.error(f"{str(e)}")


async def externalrepo():
    if Config.EXTERNAL_REPO:
        await install_externalrepo(
            Config.EXTERNAL_REPO, Config.EXTERNAL_REPOBRANCH, "xtraplugins"
        )
    """
    if Config.VCMODE:
        await install_externalrepo(Config.VC_REPO, Config.VC_REPOBRANCH, "legendvc")
"""

legend.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):
    legend.disconnect()
else:
    try:
        legend.run_until_disconnected()
    except ConnectionError:
        pass

import os

import logging

import pyrogram

from decouple import config

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',

                    level=logging.WARNING)

# vars

APP_ID = config("API_ID", default=None, cast=int)

API_HASH = config("API_HASH", default=None)

BOT_TOKEN = config("TOKEN", default=None)

if __name__ == "__main__" :

    print("Starting Bot...")

    plugins = dict(root="pyrogramee")

    app = pyrogram.Client(

        "Mrunal",

        bot_token=BOT_TOKEN,

        api_id=APP_ID,

        api_hash=API_HASH,

        plugins=plugins

    )

    app.run()

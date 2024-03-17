#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6693648608:AAE5ZMqOO9GtUzbUBDjWukV4YvyHoliiWYI")
    API_ID = int(os.environ.get("API_ID", "20810825"))
    API_HASH = os.environ.get("API_HASH", "707e67f53b4593a3e9b6b424311f84d0")
    AUTH_USERS = "6301693754"


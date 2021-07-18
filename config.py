# coding: UTF-8

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(os.getcwd(), '.env')
load_dotenv(dotenv_path)

"""==============================
Bot credential
# BOT TOKEN
=============================="""
Token = os.environ.get("DISCORD_BOT_TOKEN")



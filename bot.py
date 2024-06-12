import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6380339169:AAH5vkzcx8Y2ZaRhJURV4eEcah332uAjO0c")

API_ID = int(os.environ.get("API_ID", "11973721"))

API_HASH = os.environ.get("API_HASH", "5264bf4663e9159565603522f58d3c18")

STRING = os.environ.get("STRING", "BQC2tFkAJgkFnednb2xEwelesVA9Z9LGyBBUpjcBTA702tHOmwALkb9m0StSEubyx8fqyjYCmEk97_HO5g-0WP4ziXuLxJ2_vIgsPtjh3M-TMxdN7T_CHb6WblpJqVv6lSePLD0LQKTMp5msRyPdxV8xa0bM_LltQXOH2WjuFPpK4rnvVkrtkS5hgfdA_LdRyxn6io53fxj22GHRW4ZeZKvw_50bWgkXY5zcg3l6TDK_zKbd8YCZrfdNRHhm-o28CeMI_cB3z-DlewtsWPyqeVQV555r74Cf20KOeI4SpyTYu0ZUNqnjcnMKsMrSVnEY32QCxkcYeox6hl7OmfwNnBBoUsZMjQAAAABQ8R1WAA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()

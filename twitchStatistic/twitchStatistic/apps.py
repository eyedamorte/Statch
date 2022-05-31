from cmath import log
from django.apps import AppConfig

import threading

import os

from twitchStatistic.services.httpService import getTwitchBearer

class TwitchStatisticConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'twitchStatistic'

    def ready(self):
        
        def twitchBearer():
            bearer = getTwitchBearer()
            os.environ['TWITCH_BEARER'] = bearer['access_token']
            t = threading.Timer(bearer['expires_in'], twitchBearer)
            t.start()

        twitchBearer()
from http.client import responses
import requests

import os
from dotenv import load_dotenv
load_dotenv()
import requests

def getTwitchBearer():
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')

    url = 'https://id.twitch.tv/oauth2/token'
    params = {'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET, 'grant_type': 'client_credentials'}

    return requests.post( url, params).json()

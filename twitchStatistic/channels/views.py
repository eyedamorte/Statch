from cmath import log
import json
from django.shortcuts import render
from rest_framework.decorators import api_view


from rest_framework.response import Response 
from channels.serializes import channelsListParamsSerializer, channelsListSerializer

import os
from dotenv import load_dotenv
load_dotenv()
import requests

# Create your views here.


@api_view(['GET'])
def channels_list_get(request):
    tp_api = "https://api.twitch.tv/helix/search/channels"   


    channel = channelsListParamsSerializer(data=request.GET)
    channel.is_valid(True)

    headers = {'Authorization': 'Bearer ' + os.getenv('TWITCH_BEARER'),
                'Client-Id': os.getenv('CLIENT_ID')}

    data = {"query": request.query_params.get('query')}

    response_data = requests.get( tp_api, headers=headers, params=data).json()

    my_serializer = channelsListSerializer(data=response_data['data'], many=True)
    my_serializer.is_valid(True)
    return Response(data=my_serializer.data)

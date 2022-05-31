from cmath import log
import json
from django.shortcuts import render
from rest_framework.decorators import api_view


from rest_framework.response import Response 
from streamers.serializes import StreamersListParamsSerializer, StreamersListSerializer

import os
from dotenv import load_dotenv
load_dotenv()
import requests

# Create your views here.


@api_view(['GET'])
def streamers_list_get(request):
    tp_api = "https://api.twitch.tv/helix/search/channels"   


    channel = StreamersListParamsSerializer(data=request.GET)
    channel.is_valid(True)

    headers = {'Authorization': 'Bearer ' + os.getenv('TWITCH_BEARER'),
                'Client-Id': os.getenv('CLIENT_ID')}

    data = {"query": request.query_params.get('name')}

    response_data = requests.get( tp_api, headers=headers, params=data).json()

    my_serializer = StreamersListSerializer(data=response_data['data'], many=True)
    my_serializer.is_valid(True)
    return Response(data=my_serializer.data)

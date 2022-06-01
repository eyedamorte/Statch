from rest_framework import serializers

class channelsListSerializer(serializers.Serializer):
    id = serializers.CharField()
    display_name = serializers.CharField()
    thumbnail_url = serializers.CharField()

class channelsListParamsSerializer(serializers.Serializer):
    query = serializers.CharField()
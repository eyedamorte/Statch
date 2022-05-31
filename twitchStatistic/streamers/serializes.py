from rest_framework import serializers

class StreamersListSerializer(serializers.Serializer):
    id = serializers.CharField()
    display_name = serializers.CharField()

class StreamersListParamsSerializer(serializers.Serializer):
    name = serializers.CharField()
from rest_framework import serializers


class UserInputSerializer(serializers.Serializer):
    input = serializers.CharField()
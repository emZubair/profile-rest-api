from rest_framework import serializers


class HelloSerializers(serializers.Serializer):
    """Hello API serializers """

    name = serializers.CharField(max_length=20)
    # password = serializers.CharField(
    # max_length=100, style={'input_type': 'password'})

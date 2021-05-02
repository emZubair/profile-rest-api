from rest_framework import serializers
from profile_api.models import UserProfile


class HelloSerializers(serializers.Serializer):
    """Hello API serializers """

    name = serializers.CharField(max_length=20)
    # password = serializers.CharField(
    # max_length=100, style={'input_type': 'password'})


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializer to serialize UserProfile models objects """

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """ create and return new user """

        user = UserProfile.objects.create_user(
            email=validated_data.get('email'),
            name=validated_data.get('name'),
            password=validated_data.get('password')
        )

    def update(self, instance, validated_data):
        """ Handle updating user account """

        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

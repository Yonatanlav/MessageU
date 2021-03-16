from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from core.models import client, message


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = client
        fields = (
            'id',
            'Name',
            'PublicKey',
            'LastSeen'

        )
        read_only_fields = ['id']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = (
            'id',
            'ToClient',
            'FromClient',
            'Type',
            'Blob'

        )
        read_only_fields = ['id']
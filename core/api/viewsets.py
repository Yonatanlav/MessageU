from rest_framework import viewsets
from core.models import client,message
from .serializers import ClientSerializer, MessageSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = client.objects.all()
    serializer_class = ClientSerializer


class MessegeViewSet(viewsets.ModelViewSet):
    queryset = message.objects.all()
    serializer_class = MessageSerializer

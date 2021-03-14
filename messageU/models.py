from django.conf import settings
from django.db import models

class clinets(models.Model):
    Name = models.CharField(max_length=255)
    PublicKey = models.CharField(max_length=160)
    LastSeen = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

class messages(models.Model):
    ToClient = models.IntegerField()
    FromClient = models.IntegerField()
    Type = models.CharField(max_length=1)
    Blob = models.CharField(max_length=1)
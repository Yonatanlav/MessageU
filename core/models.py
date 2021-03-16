from django.conf import settings
from django.db import models

class client(models.Model):
    Name = models.CharField(max_length=255)
    PublicKey = models.CharField(max_length=160)
    LastSeen = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.Name

class message(models.Model):
    ToClient = models.CharField(max_length=16)
    FromClient = models.CharField(max_length=16)
    Type = models.CharField(max_length=1)
    Blob = models.CharField(max_length=1000)

    def __str__(self):
        return self.Blob
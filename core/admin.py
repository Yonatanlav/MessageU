from django.contrib import admin

# Register your models here.


from .models import client, message


admin.site.register(client)

admin.site.register(message)
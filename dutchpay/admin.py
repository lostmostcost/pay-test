from django.contrib import admin
from .models import Event, Pay, Remit, CustomUser

admin.site.register(CustomUser)
admin.site.register(Event)
admin.site.register(Pay)
admin.site.register(Remit)
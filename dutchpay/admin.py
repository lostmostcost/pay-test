from django.contrib import admin
from .models import Event, Pay, Remit, CustomUser, Member

admin.site.register(CustomUser)
admin.site.register(Member)
admin.site.register(Event)
admin.site.register(Pay)
admin.site.register(Remit)
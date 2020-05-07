from django.contrib import admin
from .models import *


class SubscriberAdmin(admin.ModelAdmin):
    class Meta:
        model = Subscriber
    # list_display = ['name', 'email',]
    list_display = [field.name for field in Subscriber._meta.fields]



admin.site.register(Subscriber, SubscriberAdmin)

from django.contrib import admin
from .models import ChatBotData

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'gender', 'service_interested')
    search_fields = ('name', 'phone', 'email', 'service_interested')

admin.site.register(ChatBotData, CustomerAdmin)
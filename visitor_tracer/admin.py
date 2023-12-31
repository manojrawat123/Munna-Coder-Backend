from django.contrib import admin
from visitor_tracer.models import Visitor

class UserTracerAdmin(admin.ModelAdmin):
    fields = ["website_accessed", "sup_id_adress"]
    # prepopulated_fields = {'slug': ('website_accessed')}

admin.site.register(Visitor, UserTracerAdmin)
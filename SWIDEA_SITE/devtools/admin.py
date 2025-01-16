from django.contrib import admin
from devtools.models import DevTool

@admin.register(DevTool)
class DevToolAdmin(admin.ModelAdmin):
    list_display = ['name', 'kind']
    search_fields = ['name', 'kind']

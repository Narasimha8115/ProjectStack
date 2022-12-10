from os import name
from django.contrib import admin
from .models import Projectss,Profile_Up
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.
admin.site.register(Projectss,ImportExportActionModelAdmin)
admin.site.register(Profile_Up)




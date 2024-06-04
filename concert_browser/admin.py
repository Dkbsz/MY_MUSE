from django.contrib import admin
from .models import CustomUser, Location, Concert
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Location)
admin.site.register(Concert)

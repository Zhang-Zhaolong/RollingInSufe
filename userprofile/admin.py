from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'telephone', 'school', 'major']
    fields = ['user', 'telephone', 'birthday', 'major', 'school', 'photo']


admin.site.register(Profile, ProfileAdmin)


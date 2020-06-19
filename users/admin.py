from django.contrib import admin
from . import models
from django.contrib.admin import ModelAdmin
# Register your models here.
admin.site.register(models.Profile)

admin.site.register(models.Roles)



@admin.register(models.UserRoles)
class UserRoleAdmin(ModelAdmin):
    list_display = ( "user", "role", )
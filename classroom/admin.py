from django.contrib import admin

from django.contrib.admin import ModelAdmin
from . import models
# Register your models here.

admin.site.register(models.Question)

admin.site.register(models.UserClassQuestion)




@admin.register(models.Class)
class ClassAdmin(ModelAdmin):
    list_display = ("id", "name", "start_time", "end_time")

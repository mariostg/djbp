from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from project import models

admin.site.register(models.ProjectUser, UserAdmin)

# admin.site.register()

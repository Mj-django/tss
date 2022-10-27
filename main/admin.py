from django.contrib import admin

# Register your models here.
from . import models
# Register your models here.

admin.site.register(models.user)
admin.site.register(models.user_as)
from django.contrib import admin

# Register your models here.
from .models import User

#registro
admin.site.register(User)
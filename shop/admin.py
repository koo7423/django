from django.contrib import admin
from .models import shop

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(shop, UserAdmin)
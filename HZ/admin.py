from django.contrib import admin

class own_productionAdmin(admin.ModelAdmin):
    list_display = ['name', 'articul', 'kolichestvo', 'color', 'size', 'user_name']

class user1Admin(admin.ModelAdmin):
    list_display = ['user_name', 'last_name', 'otdel']

class Articl1Admin(admin.ModelAdmin):
    list_display = ['title', 'anons', 'date']


# Register your models here.
from .models import Autorization
admin.site.register(Autorization)

from.models import own_production
admin.site.register(own_production, own_productionAdmin)

from.models import user1
admin.site.register(user1, user1Admin)

from.models import Articl
admin.site.register(Articl, Articl1Admin)


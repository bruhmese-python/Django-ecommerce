from django.contrib import admin
from .models import *
# Register your models here.


class categAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']


admin.site.register(categ, categAdmin)


class prodAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug', 'price', 'stock', 'img']


admin.site.register(product, prodAdmin)

from django.contrib import admin

from .models import *


class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('content',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Cat, CatAdmin)
admin.site.register(Collection, CollectionAdmin)

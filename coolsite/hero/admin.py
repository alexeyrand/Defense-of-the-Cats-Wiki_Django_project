from django.contrib import admin

from .models import *


class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('content',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug":("name",)}

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug":("name",)}

admin.site.register(Cat, CatAdmin)
admin.site.register(Collection, CollectionAdmin)

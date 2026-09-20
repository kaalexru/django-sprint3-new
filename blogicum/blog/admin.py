from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Category, Location, Post


admin.site.empty_value_display = 'Не задано'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'category',
        'location',
        'is_published',
    )
    list_editable = (
        'category',
        'location',
        'is_published',
    )
    search_fields = ('title', 'text')
    list_filter = ('is_published', 'category', 'location')
    list_display_links = ('title',)
    list_select_related = ('author', 'category', 'location')
    date_hierarchy = 'pub_date'


admin.site.register(Category)
admin.site.register(Location)
admin.site.unregister(Group)

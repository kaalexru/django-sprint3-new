from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.db.models import Count

from .models import Category, Location, Post


User = get_user_model()

admin.site.empty_value_display = 'Не задано'
admin.site.unregister(User)


@admin.register(User)
class BlogicumUserAdmin(UserAdmin):
    list_display = (*UserAdmin.list_display, 'posts_count')

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            posts_count=Count('posts'),
        )

    @admin.display(
        description='Количество публикаций',
        ordering='posts_count',
    )
    def posts_count(self, user):
        return user.posts_count


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

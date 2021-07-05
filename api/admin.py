"""
Additional features for admin area providing comfortable management of
project content

"""
from django.contrib import admin

from api.models import Category, Comment, Genre, Review, Title, User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'role')
    empty_value_display = ' - '


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'category')
    search_fields = ('name', )
    list_filter = ('year', )
    empty_value_display = ' - '


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name')
    search_fields = ('slug', )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'title', 'author', 'text', 'score')
    search_fields = ('title', 'text')
    list_filter = ('pub_date', 'author')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'review', 'author', 'text', )
    search_fields = ('review', 'text', )
    list_filter = ('pub_date', 'author', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)

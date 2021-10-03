from django.contrib import admin
from .models import *

# admin.site.register(Post)


# admin.site.register(Category)
# admin.site.register(Comment)
# admin.site.register(PostView)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'timestamp']
    search_fields = ['title', 'content']

# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ['user']
    
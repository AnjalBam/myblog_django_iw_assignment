from django.contrib import admin

from .models import Author, BlogPost


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published_at', 'last_modified', 'author')
    search_fields = ('title', 'slug', 'author')
    prepopulated_fields = {
        'slug': ('title',)
    }


admin.site.register(Author, AuthorAdmin)
admin.site.register(BlogPost, BlogPostAdmin)


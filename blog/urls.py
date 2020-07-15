from django.urls import path

from .views import home_view, author_list_view, blog_view, create_blog

app_name = 'blog'
urlpatterns = [
    path('', home_view, name='home'),
    path('authors/', author_list_view, name='authors_list'),
    path('create/', create_blog, name='create'),
    path('blog-post/<slug:blog_slug>', blog_view, name='blog'),
]
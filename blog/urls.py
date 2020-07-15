from django.urls import path

from .views import home_view, author_list_view

app_name = 'blog'
urlpatterns = [
    path('', home_view, name='home'),
    path('authors/', author_list_view, name='authors_list')
]
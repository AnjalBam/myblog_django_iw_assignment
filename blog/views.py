from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from .models import Author, BlogPost

# Create your views here.


def home_view(request):
    posts = get_list_or_404(BlogPost)
    print(posts)
    context = {}
    return render(request, 'blog/index.html', context=context)

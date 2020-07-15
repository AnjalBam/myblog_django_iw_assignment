from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from .models import Author, BlogPost

# Create your views here.


def home_view(request):
    posts = get_list_or_404(BlogPost)
    # print(posts)
    context = {'posts': posts}
    return render(request, 'blog/index.html', context=context)


def author_list_view(request):
    authors = get_list_or_404(Author)
    # print(authors)
    context = { 'authors': authors }
    return render(request, 'blog/author-list.html', context=context)
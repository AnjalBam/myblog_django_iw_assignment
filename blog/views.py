from django.shortcuts import(render, get_list_or_404,
                              get_object_or_404, reverse)
from django.http import HttpResponsePermanentRedirect
from .models import Author, BlogPost
from .forms import CreateBlogForm

# Create your views here.


def home_view(request):
    # posts = get_list_or_404(BlogPost)
    posts = BlogPost.objects.all()

    # print(posts)
    context = {'posts': posts}
    return render(request, 'blog/index.html', context=context)


def author_list_view(request):
    # authors = get_list_or_404(Author)
    authors = Author.objects.all()

    # print(authors)
    context = {'authors': authors }
    return render(request, 'blog/author-list.html', context=context)


def blog_view(request, blog_slug):
    blog = get_object_or_404(BlogPost, slug=blog_slug)
    # print(blog)
    context = {
        'blog': blog
    }
    return render(request, 'blog/blog.html', context=context)


def create_slug(string):
    s = string.lower()
    words = s.split(' ')
    slug = '-'.join(words)
    return slug


def create_blog(request):
    if request.method == 'POST':
        form = CreateBlogForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.slug = create_slug(form.title)
            form.save()
            return HttpResponsePermanentRedirect(reverse('blog:home'))
    else:
        form = CreateBlogForm()
    context = {
        'form': form
    }
    return render(request, 'blog/create-blog.html', context=context)

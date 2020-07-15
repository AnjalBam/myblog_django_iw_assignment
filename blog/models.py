from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               related_name='blog_posts')
    published_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-published_at',)

    def __str__(self):
        return f"{self.title[:20]}... - {self.author}"

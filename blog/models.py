
from django.contrib.auth.models import User
from django.db import models
from django.db.models.functions import datetime
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.title}'


class Article(models.Model):
    title = models.CharField(max_length=20, help_text="It should be unique")
    text = models.TextField()
    image = models.ImageField(upload_to='article/image')
    category = models.ManyToManyField(Category, related_name='articles')
    banner = models.ImageField(upload_to='article/banner', help_text='best size for banner:770x340')
    status = models.BooleanField(default=False)
    slug = models.SlugField(null=True, unique=True, blank=True, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={"slug": self.slug})

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments' , null=True , blank=True)
    
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)

    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}------{self.text[:30]}"






class Message(models.Model):
    name = models.CharField(max_length=10)
    text = models.TextField()
    email = models.EmailField(null=True)
    created = models.DateTimeField(auto_now_add=True)



from django.shortcuts import render, get_object_or_404
from .models import Article


def index(request):
    article = Article.objects.filter(status=True)
    article_ordring = Article.objects.all()[:3]

    return render(request , 'blog/index.html' , {'objects':article , 'article_ordring':article_ordring })


def article(request):
    article = Article.objects.filter(status=True)
    return render(request , 'blog/blog.html' , {'objects':article})

def article_detail(request, slug):
    article = get_object_or_404(Article , slug=slug)
    return render(request , 'blog/article-details.html' ,{'objects':article})


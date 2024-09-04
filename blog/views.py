from django.shortcuts import render, get_object_or_404
from .models import Article ,Category
from django.core.paginator import Paginator


def index(request):
    article = Article.objects.filter(status=True)
    article_ordring = Article.objects.all()[:3]

    return render(request , 'blog/index.html' , {'objects':article , 'article_ordring':article_ordring })


def article(request):
    article = Article.objects.filter(status=True)
    paginator = Paginator(article, 1)  # Show 4 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request , 'blog/blog.html' , {'objects':page_obj})



def article_detail(request, slug):
    article = get_object_or_404(Article , slug=slug)
    return render(request , 'blog/article-details.html' ,{'objects':article})


def category_detail(request , pk=None):
    category = get_object_or_404(Category  , id=pk)
    articles = category.articles.all()

    return render(request , 'blog/blog.html' , {'objects':articles})
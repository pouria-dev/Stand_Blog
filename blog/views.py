from django.shortcuts import render
from .models import Article



def index(request):
    article = Article.objects.filter(status=True)
    return render(request , 'blog/index.html' , {'objects':article })

def article_detail(request,pk):
    article = Article.objects.get(id=pk)
    return render(request , 'blog/article-details.html' ,{'objects':article})
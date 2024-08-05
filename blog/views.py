from django.shortcuts import render
from .models import Article
def index(request):
    article = Article.objects.filter(status=True)
    return render(request, 'blog/index.html' , {"objects":article})

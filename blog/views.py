from django.shortcuts import render, get_object_or_404, redirect
from .models import Article ,Category
from .forms import Contact_Form
from django.core.paginator import Paginator
from .models import Comment , Message
from django.urls import reverse

def index(request):
    article = Article.objects.filter(status=True)
    article_ordring = Article.objects.all()[:3]

    return render(request , 'blog/index.html' , {'objects':article , 'article_ordring':article_ordring })

def contact(request):
    if request.method == "POST":
        forms = Contact_Form(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            text = forms.cleaned_data['text']
            Message.objects.create(name=name ,text=text )

            return redirect(reverse('blog:home'))
    form = Contact_Form()
    return render(request , 'blog/contact.html' , {'form': form} )

def article(request):
    article = Article.objects.filter(status=True)
    paginator = Paginator(article, 1)  # Show 4 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request , 'blog/blog.html' , {'objects':page_obj})



def article_detail(request, slug):
    article = get_object_or_404(Article , slug=slug)
    if request.method == "POST":
        text = request.POST.get('text')
        Comment.objects.create(post=article , author=request.user ,text = text)
    return render(request , 'blog/article-details.html' ,{'objects':article})


def category_detail(request , pk=None):
    category = get_object_or_404(Category  , id=pk)
    articles = category.articles.all()

    return render(request , 'blog/blog.html' , {'objects':articles})
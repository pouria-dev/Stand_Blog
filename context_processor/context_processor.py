from blog.models import Article , Category
def recent_article(request):

    recent = Article.objects.order_by('-created')

    return {'recent':recent}

def article_category(request):
    category = Category.objects.all()

    return {'category':category}
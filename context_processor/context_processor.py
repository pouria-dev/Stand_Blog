from blog.models import Article
def recent_article(request):

    recent = Article.objects.order_by('-created')

    return {'recent':recent}
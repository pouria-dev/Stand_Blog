from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=15)
class Article(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    image = models.ImageField(upload_to='article')
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    banner = models.ImageField(upload_to='article' ,help_text='best size for banner:770x340')

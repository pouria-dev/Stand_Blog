from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.title}'


class Article(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    image = models.ImageField(upload_to='article/image')
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    banner = models.ImageField(upload_to='article/banner' ,help_text='best size for banner:770x340')
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'


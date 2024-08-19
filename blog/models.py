from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.title}'


class Article(models.Model):
    title = models.CharField(max_length=20 ,help_text="It should be unique")
    text = models.TextField()
    image = models.ImageField(upload_to='article/image')
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    banner = models.ImageField(upload_to='article/banner' ,help_text='best size for banner:770x340')
    status = models.BooleanField(default=False)
    slug = models.SlugField(null=True , unique=True ,blank=True,default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
    def get_absolute_url(self):
        return reverse('blog:detail' , kwargs={"slug":self.slug})

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Article , self).save()


    def __str__(self):
        return f'{self.title}'

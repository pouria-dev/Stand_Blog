from django.urls import path
from .views import index ,article ,  article_detail , category_detail

app_name='blog'

urlpatterns = [
    path('' , index , name='home'),
    path('all' , article , name='articles'),
    path('detail/<slug:slug>' , article_detail , name='detail'),
    path('category/<int:pk>' , category_detail , name='category')
]
from django.urls import path
from .views import index ,article ,  article_detail

app_name='blog'

urlpatterns = [
    path('' , index , name='home'),
    path('all' , article , name='articles'),
    path('detail/<slug:slug>' , article_detail , name='detail'),
]
from django.urls import path
from .views import index , article_detail

app_name='blog'

urlpatterns = [
    path('' , index , name='home'),

    path('detail/<int:pk>' , article_detail , name='detail'),
]
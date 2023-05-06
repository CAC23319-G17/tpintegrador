from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('products/all', views.prod_all,name='prodall'),
    path('products/popular', views.prod_pop,name='prodpopular'),
    path('products/news', views.prod_news,name='prodnews'),
]
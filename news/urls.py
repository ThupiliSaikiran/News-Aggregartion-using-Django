from django.urls import path
from . import views


urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('feeds/new/', views.new_feed, name='feed_new'),
    path('feeds/', views.feeds_list, name='feeds_list'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('posts/',views.post_list,name='posts'),
    path('posts/<int:pk>/',views.post_detail,name='post_detail'),
    path('posts/create/',views.create_post,name='create_post'),
    path('topics/<int:pk>/',views.topic_posts,name='topic'),
    path('browse/',views.browse,name='browse'),
]
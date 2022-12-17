from django.urls import path
from .views import (
    PostListView,
    PostDetailtView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView)
from . import views
urlpatterns=[
    path('',PostListView.as_view(),name='blog-home'),
    path('user/<username>',UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/',PostDetailtView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('about/',views.about,name='blog-about') 
]
# handler404 = 'blog.views.error404'
# handler404 = 'blog.views.error404'
# handler500='blog.views.error500'
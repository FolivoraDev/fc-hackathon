from django.urls import path

from .views import PostListView, PostCreateView, comment_create_view

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('create_post/', PostCreateView.as_view(success_url='/posts'), name='post-create'),
    path('create_comment/<int:pk>/', comment_create_view, name='comment-create'),
]

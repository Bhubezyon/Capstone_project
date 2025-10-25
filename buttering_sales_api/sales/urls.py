from django.urls import path
from .views import (
    RegisterView, LoginView, ProfileView, PostListCreateView, PostDetailView,
    CommentListCreateView, CommentDetailView, LikeView, UnlikeView, FollowView, UnfollowView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user_register'),
    path('login/', LoginView.as_view(), name='user_login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('posts/<int:post_id>/like/', LikeView.as_view(), name='like-post'),
    path('posts/<int:post_id>/unlike/', UnlikeView.as_view(), name='unlike-post'),
    path('users/<int:user_id>/follow/', FollowView.as_view(), name='follow-user'),
    path('users/<int:user_id>/unfollow/', UnfollowView.as_view(), name='unfollow-user'),
]
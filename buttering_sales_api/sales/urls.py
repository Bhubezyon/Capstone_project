from django.urls import path
from .views import RegisterView, LoginView, ProfileView
from .views import FollowUserView, UnfollowUserView, LikeUserView, UnlikeUserView

urlpatterns = [
    path('api/admin', admin.site.urls),
    path('api/sales', include('sales.url')),
    path('api/posts', include('posts.urls')) 
]

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
    path('like/<int:user_id>/', LikeUserView.as_view(), name='like_user'),
    path('unlike/<int:user_id>/', UnlikeUserView.as_view(), name='unlik_user'),
]
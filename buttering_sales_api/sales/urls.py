from django.urls import path, include
from .views import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sales', include('sales.url')),
    path('api/posts', include('posts.urls')),
]

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user_register'),
    path('login/', LoginView.as_view(), name='user_login'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='user_profile'),
    path('', PostListCreateView.as_view(), name='post_list_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', MessageListView.as_view(), name='message_list'),
    path('send/', SendMessageView.as_view(), name='send_message'),
    path('follow/<int:user_id/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
    path('like/<int:user_id>/', LikeUserView.as_view(), name='like_user'),
    path('unlike/<int:user_id>/', UnlikeUserView.as_view(), name='unlik_user'),
]
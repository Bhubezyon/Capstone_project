from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'register', RegisterViewSet)
router.register(r'login', LoginViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users', include(users.urls)),
    path('api/post', include('posts.urls')),
    path('api/message', include('message.urls')),
    path('api/register', RegisterView.as_view(), name='register'),
    path('api/login', LoginView.as_view(), name='login'),
    path('api/message', MessageListCreateView.as_view(), name='message_list_create')
]

urlpatterns += [
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike_post'),
]

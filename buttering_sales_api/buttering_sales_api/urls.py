from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, NotificationViewSet, MessageViewSet
from .views_user import RegisterView
from django.contrib import admin

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('api/register', include('register.urls')),
    path('api/login', include('login.urls')),
    path('admin/', admin.site.urls),
    path('api/sales/', include('sale.urls')),
    path('api/users/', include('user.urls')),
    path('api/messages/', include('message.urls')),
    path('api/routers', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login', LoginView.as_view(), name='login')
]
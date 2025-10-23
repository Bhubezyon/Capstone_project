from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', include('register.urls')),
    path('api/login/', include('login.urls')),
    path('api/profile/', include('profile.urls')),
    path('api/post/', include('post.urls')),
    path('api/comments/', include('comments.urls')),
    path('api/messages/', include('messages.urls')),
    path('api/likes/', include('likes.urls')),
    path('api/followers/', include('followers.urls')),
    path('api/notifications/', include('notifications.urls')),  
    path('api/search/', include('search.urls')),
    path('api/notifications/', include('notifications.urls')),
]
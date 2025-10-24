from django.urls import path, include
from django.contrib import admin
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h2>Welcome to the Buttering Sales API</h2><p>Visit <a href='#'>Home</a></p>Visit <a href='/api/'>API/</a> for API endpoints.</p>")

urlpatterns = [
    path('', home),
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
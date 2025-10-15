from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('sales.urls')),
    path('api/', homepage, name='home')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
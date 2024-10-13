from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram_2024.common.urls')),
    path('accounts/', include('petstagram_2024.accounts.urls')),
    path('pets/', include('petstagram_2024.pets.urls')),
    path('photos/', include('petstagram_2024.photos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
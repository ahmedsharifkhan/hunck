from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import include, url
# import certbot_django.server.urls

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # url(r'^\.well-known/', include(certbot_django.server.urls)),
    path('admin', admin.site.urls),
    path('', include('blog.urls')),

    # path('employees/', include('employees.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
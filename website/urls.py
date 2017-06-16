from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import notifications.urls

urlpatterns = [
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^jet/', include('jet.urls', 'jet')),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    url(r'^admin/', admin.site.urls),

    url(r'^music/', include('music.urls')),
    url(r'^', include('music.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

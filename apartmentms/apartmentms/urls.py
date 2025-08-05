from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('flats/', include('flats.urls')),
    path('residents/', include('residents.urls')),
    path('billing/', include('billing.urls')),
    path('documents/', include('documents.urls')),
    path('electricity/', include('electricity.urls')),
    path('infrastructure/', include('infrastructure.urls')),
    path('complaints/', include('complaints.urls')),
    path('visitors/', include('visitors.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

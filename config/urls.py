from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

from core.views import (
    ParkViewSet,
    TrailViewSet,
    EventViewSet,
    AvailabilityViewSet,
    WaterfallViewSet,
    BiodiversityViewSet,
    home,
    parks_view,
    trails_view,
    events_view,
    park_detail,
    waterfalls_view,
    biodiversity_view
)

router = DefaultRouter()
router.register(r'parks', ParkViewSet)
router.register(r'trails', TrailViewSet)
router.register(r'events', EventViewSet)
router.register(r'availability', AvailabilityViewSet)
router.register(r'waterfalls', WaterfallViewSet)
router.register(r'biodiversity', BiodiversityViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # páginas
    path('', home),
    path('parks-page/', parks_view),
    path('trails-page/', trails_view),
    path('events-page/', events_view),
    path('parks-page/<int:park_id>/', park_detail),
    path('waterfalls-page/', waterfalls_view),
    path('biodiversity-page/', biodiversity_view),

    # API
    path('api/', include(router.urls)),
]

# media (imagens)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
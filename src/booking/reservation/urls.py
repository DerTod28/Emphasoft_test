from rest_framework.routers import DefaultRouter

from .views import ReservationViewSet

router = DefaultRouter()
router.register('', ReservationViewSet, basename='room_reservations')

urlpatterns = router.urls

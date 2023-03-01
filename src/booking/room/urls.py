from django.urls import path
from .views import RoomViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', RoomViewSet, basename='room')
urlpatterns = router.urls

urlpatterns += [
    # path('', RoomViewSet, name='room_list_api'),
]

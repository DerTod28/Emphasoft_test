from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import RoomViewSet

router = DefaultRouter()
router.register('', RoomViewSet, basename='room')
urlpatterns = router.urls

urlpatterns += [
    # path('', RoomViewSet, name='room_list_api'),
]

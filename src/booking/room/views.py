from rest_framework import permissions, viewsets

from booking.utils.views_mixin import PermissionsMixin

from .filters import DateRangeFilterSet
from .models import Room
from .serializers import RoomSerializer


class RoomViewSet(PermissionsMixin, viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filterset_class = DateRangeFilterSet
    ordering_fields = ['price', 'capacity']
    action_permissions = {
        'list': [permissions.AllowAny],
        'retrieve': [permissions.AllowAny]
    }

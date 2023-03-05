from rest_framework import permissions, viewsets

from booking.utils.views_mixin import PermissionsMixin

from .filters import DateRangeFilterSet
from .models import Room
from .serializers import RoomSerializer


class RoomViewSet(PermissionsMixin, viewsets.ModelViewSet):
    """
    Methods for Room instance.
    Create, patch, put, delete only for admin, make sure you have the right jwt.
    Filtering - price, capacity and free rooms - available_after and available_before
    For ordering choices are - price and capacity
    """
    permission_classes = [permissions.IsAdminUser]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filterset_class = DateRangeFilterSet
    ordering_fields = ['price', 'capacity']
    action_permissions = {
        'list': [permissions.AllowAny],
        'retrieve': [permissions.AllowAny]
    }

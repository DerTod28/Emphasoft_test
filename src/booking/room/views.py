from rest_framework import mixins, permissions, viewsets

from booking.room.filters import RoomFilterSet
from booking.room.models import Room
from booking.room.serializers import RoomSerializer


class RoomViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    """
    Methods for Room instance.
    Filtering - price, capacity and free rooms - available_after and available_before
    For ordering choices are - price and capacity
    """
    permission_classes = [permissions.AllowAny]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filterset_class = RoomFilterSet
    ordering_fields = ['price', 'capacity']

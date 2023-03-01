from rest_framework import permissions
from rest_framework import viewsets

from .mixins import PermissionsMixin
from .models import Room
from .serializers import RoomSerializer


class RoomViewSet(PermissionsMixin, viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    action_permissions = {'list': [permissions.AllowAny]}

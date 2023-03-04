from rest_framework import viewsets, mixins, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from booking.utils.views_mixin import PermissionsMixin
from .models import Reservation, RoomReservation
from .serializers import ReservationCreateSerializer, ReservationRoomSerializer


class ReservationViewSet(
    PermissionsMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Reservation.objects.prefetch_related('roomreservation_set')
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ReservationCreateSerializer

    action_permissions = {
        'retrieve': [permissions.IsAdminUser]
    }

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()

        if user.is_superuser:
            return queryset
        else:
            return queryset.filter(guest=user)

    @action(detail=True, methods=['PATCH'])
    def cancel(self, request, pk):
        instance = self.get_object()

        qs = instance.roomreservation_set.all()
        for i in qs:
            i.status = RoomReservation.StatusType.CANCELED
            i.save()

        serialized_data = {'data': ReservationRoomSerializer(qs, many=True).data}
        return Response(status=status.HTTP_201_CREATED, data=serialized_data)

import logging

from django.db.models import Prefetch
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Reservation, RoomReservation
from .serializers import ReservationSerializer


class ReservationViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    Methods for Reservation instance.
    Retrieve only for admin, make sure you have the right jwt.
    """
    queryset = Reservation.objects.prefetch_related(
        Prefetch(
            'roomreservation_set', queryset=RoomReservation.objects.select_related('room')
        )
    ).select_related('guest')
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ReservationSerializer

    def get_queryset(self) -> queryset:
        """
        Returns user's reservations, if user is admin - shows all Reservation objects
        """
        user = self.request.user
        queryset = super().get_queryset()

        if user.is_superuser:
            return queryset
        else:
            return queryset.filter(guest=user)

    @action(detail=True, methods=['PATCH'])
    def cancel(self, request: Request, pk: int) -> Response:
        """
        Change reservation status to 'canceled' for rooms in reservation
        """
        RoomReservation.objects.filter(
            reservation_id=pk
        ).exclude(
            status=RoomReservation.StatusType.CANCELED
        ).update(status=RoomReservation.StatusType.CANCELED)

        serializer = self.get_serializer(self.get_object())
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

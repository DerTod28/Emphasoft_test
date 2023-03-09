from django.contrib.auth.models import User
from rest_framework import serializers

from booking.reservation.models import Reservation, RoomReservation
from booking.room.models import Room


class ReservationRoomRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'number', 'price']


class ReservationRoomSerializer(serializers.ModelSerializer):
    room = ReservationRoomRoomSerializer()

    class Meta:
        model = RoomReservation
        fields = ['id', 'room', 'status']


class ReservationGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class ReservationSerializer(serializers.ModelSerializer):
    guest = ReservationGuestSerializer(read_only=True)
    rooms = ReservationRoomSerializer(
        many=True,
        read_only=True,
        source='roomreservation_set'
    )
    room_ids = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(), many=True,
        write_only=True, source='room'
    )

    class Meta:
        model = Reservation
        fields = ['id', 'guest', 'start_date', 'end_date', 'rooms', 'room_ids']

    def validate(self, attrs):
        if self.partial:
            return attrs

        attrs['guest'] = self.context['request'].user

        if attrs['end_date'] <= attrs['start_date']:
            raise serializers.ValidationError(
                'end_date has to be greater than start_date.'
            )

        if RoomReservation.objects.filter(
                reservation__start_date__lt=attrs['end_date'],
                reservation__end_date__gt=attrs['start_date'],
                room__in=attrs['room'],
                status=RoomReservation.StatusType.APPROVED
        ).exists():
            raise serializers.ValidationError('Room is already reserved.')

        return attrs

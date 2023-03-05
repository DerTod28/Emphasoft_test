from rest_framework import serializers

from ..room.models import Room
from .models import Reservation, RoomReservation


class RoomReservationRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'number', 'price']


class ReservationRoomSerializer(serializers.ModelSerializer):
    room = RoomReservationRoomSerializer()

    class Meta:
        model = RoomReservation
        fields = ['id', 'room', 'price', 'status']


class ReservationCreateSerializer(serializers.ModelSerializer):
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
        guest = serializers.PrimaryKeyRelatedField(read_only=True)
        fields = ['id', 'guest', 'start_date', 'end_date', 'rooms', 'room_ids']
        extra_kwargs = {'guest': {'required': False},
                        'date_range': {'required': False}
                        }

    def validate(self, attrs):
        attrs['guest'] = self.context['request'].user
        attrs['date_range'] = attrs['start_date'], attrs['end_date']

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

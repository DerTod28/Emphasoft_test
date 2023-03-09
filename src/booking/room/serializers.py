from rest_framework import serializers

from booking.room.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'number', 'price', 'capacity']

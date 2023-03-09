import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status

from booking.room.models import Room


@pytest.mark.django_db
def test_get_rooms_with_filter(client):
    room_data = [
        {
            'number': 1,
            'price': 1500,
            'capacity': 1,
        },
        {
            'number': 2,
            'price': 1700,
            'capacity': 1,
        },
    ]
    for data in room_data:
        Room.objects.create(**data)
    url = '/rooms/'
    data = {
        'price': '1500'
    }
    expected_response = Room.objects.filter(price=data['price'])
    response = client.get(url=url, data=data, path=url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == len(expected_response)


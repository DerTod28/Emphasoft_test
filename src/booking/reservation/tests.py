import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status

from booking.room.models import Room


@pytest.mark.django_db
def test_make_free_room_reservation(client):
    url = reverse('token_obtain_pair')

    user_credentials = {
        'username': 'username',
        'password': 'password',
        'email': 'email@email.ru'
    }

    User.objects.create_user(**user_credentials)

    response = client.post(
        url,
        {
            'username': user_credentials['username'],
            'password': user_credentials['password']
        }
    )

    access_token = response.data['access']

    room_data = {
        'number': 1,
        'price': 1500,
        'capacity': 1,
    }

    room = Room.objects.create(**room_data)

    url = '/reservations/'

    reservation_data = {
        'guest': 1,
        'start_date': '2023-03-05',
        'end_date': '2023-03-06',
        'room_ids': [room.id]
    }

    response = client.post(
        path=url,
        data=reservation_data,
        content_type='application/json',
        **{'HTTP_AUTHORIZATION': f'Bearer {access_token}'}
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_another_user_reservations(client):
    url = reverse('token_obtain_pair')

    user_credentials = {
        'username': 'username',
        'password': 'password',
        'email': 'email@email.ru'
    }

    User.objects.create_user(**user_credentials)

    response = client.post(
        url,
        {
            'username': user_credentials['username'],
            'password': user_credentials['password']
        }
    )

    access_token = response.data['access']

    room_data = {
        'number': 1,
        'price': 1500,
        'capacity': 1,
    }

    room = Room.objects.create(**room_data)

    url = '/reservations/'

    reservation_data = {
        'start_date': '2023-03-05',
        'end_date': '2023-03-06',
        'room_ids': [room.id]
    }

    client.post(
        path=url,
        data=reservation_data,
        content_type='application/json',
        **{'HTTP_AUTHORIZATION': f'Bearer {access_token}'}
    )

    user_2_credentials = {
        'username': 'username_2',
        'password': 'password_2',
        'email': 'email@email.ru'
    }

    User.objects.create_user(**user_2_credentials)

    url = reverse('token_obtain_pair')

    response = client.post(
        url,
        {
            'username': user_2_credentials['username'],
            'password': user_2_credentials['password']
        }
    )

    access_token = response.data['access']

    url = '/reservations/'

    response = client.get(
        path=url,
        data=reservation_data,
        content_type='application/json',
        **{'HTTP_AUTHORIZATION': f'Bearer {access_token}'}
    )

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 0

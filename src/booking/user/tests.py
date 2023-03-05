import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_register_user(client):
    url = reverse('auth_signup')
    data = {
        'username': 'username',
        'password': 'password',
        'email': 'user@example.com',
        'first_name': 'firstname',
        'last_name': 'lastname'
    }
    response = client.post(url=url, data=data, path=url)

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_invalid_field(client):
    url = reverse('token_obtain_pair')

    user_credentials = {
        'username': 'username',
        'password': 'password',
        'email': 'email@email.ru'
    }

    user = User.objects.create_user(**user_credentials)

    response = client.post(
        url, {
            'email': user_credentials['email'],
            'password': user_credentials['password']
        },
        format='json'
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_get_token_pair(client):
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

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_current_user(client):
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

    url = reverse('current_user')

    response = client.get(
        url,
        content_type='application/json',
        **{'HTTP_AUTHORIZATION': f'Bearer {access_token}'}
    )

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_user_without_token(client):
    access_token = 'no_token'

    url = reverse('current_user')

    response = client.get(
        url,
        content_type='application/json',
        **{'HTTP_AUTHORIZATION': f'Bearer {access_token}'}
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED

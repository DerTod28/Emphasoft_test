from django.contrib.auth.models import User
from django.db import models
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _

from booking.room.models import Room
from booking.utils.models_mixin import TimeStampedMixin


class Reservation(TimeStampedMixin):
    guest = models.ForeignKey(User, models.DO_NOTHING, verbose_name='Гость')
    start_date = models.DateField(verbose_name='Дата заезда')
    end_date = models.DateField(verbose_name='Дата выезда')
    room = models.ManyToManyField(Room, through='RoomReservation')

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'


class RoomReservation(TimeStampedMixin):
    class StatusType(models.TextChoices):
        APPROVED = 'APPROVED', _('Approved')
        PENDING = 'PENDING', _('Pending')
        CANCELED = 'CANCELED', _('Canceled')

    reservation = models.ForeignKey(
        Reservation, models.DO_NOTHING, verbose_name='Бронирование'
    )
    room = models.ForeignKey(Room, models.DO_NOTHING, verbose_name='Комната')
    status = models.CharField(
        max_length=30, choices=StatusType.choices,
        default='PENDING', verbose_name='Статус бронирования'
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=('reservation', 'room'), name='reservation_room_unique'
            )
        ]
        verbose_name = 'Бронирование комнаты'
        verbose_name_plural = 'Бронирования комнат'

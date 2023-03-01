from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .mixins import TimeStampedMixin, UUIDMixin


class RoomType(UUIDMixin, TimeStampedMixin):
    name = models.CharField(max_length=150, verbose_name='Тип комнаты')

    class Meta:
        verbose_name = 'Тип комнаты'
        verbose_name_plural = 'Типы комнаты'

    def __str__(self):
        return self.name


class Room(UUIDMixin, TimeStampedMixin):
    number = models.IntegerField(verbose_name='Номер комнаты',
                                 validators=[
                                     MaxValueValidator(400),
                                     MinValueValidator(1)
                                 ]
                                 )
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Стоимость')
    capacity = models.IntegerField(verbose_name='Вместимость',
                                   validators=[
                                       MaxValueValidator(10),
                                       MinValueValidator(1)
                                   ]
                                   )
    type = models.ForeignKey(RoomType, models.DO_NOTHING, verbose_name='Тип комнаты')

    class Meta:
        unique_together = (
            ('number', 'type')
        )

        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def __str__(self):
        return ' - '.join([str(self.number), self.type.name])


class Reservation(UUIDMixin, TimeStampedMixin):
    guest = models.ForeignKey(User, models.DO_NOTHING, verbose_name='Гость')
    start_date = models.DateField(verbose_name='Дата заезда')
    end_date = models.DateField(verbose_name='Дата выезда')
    room = models.ManyToManyField(Room, through='RoomReservation')

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'


class RoomReservation(UUIDMixin, TimeStampedMixin):
    reservation = models.ForeignKey(Reservation, models.DO_NOTHING, verbose_name='Бронирование')
    room = models.ForeignKey(Room, models.DO_NOTHING, verbose_name='Комната')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Общая стоимость')
    ROOM_RESERVATION_STATUS_CHOICES = [
        ('APPROVED', 'Одобрено'),
        ('PENDING', 'Рассматривается'),
        ('CANCELED', 'Отменено'),
    ]
    status = models.CharField(max_length=30, choices=ROOM_RESERVATION_STATUS_CHOICES,
                              default='PENDING', verbose_name='Статус бронирования')

    @property
    def calculate_total_price(self):
        calculated_days = self.reservation.end_date - self.reservation.start_date
        total_price = self.room.price * calculated_days.days
        print(calculated_days)
        print(total_price)
        return total_price

    def save(self, *args, **kwargs):
        self.price = self.calculate_total_price
        super(RoomReservation, self).save(*args, **kwargs)

    class Meta:
        unique_together = (
            ('reservation', 'room')
        )

        verbose_name = 'Бронирование комнаты'
        verbose_name_plural = 'Бронирования комнат'

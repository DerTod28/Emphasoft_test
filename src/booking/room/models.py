from django.core.validators import MinValueValidator
from django.db import models

from booking.utils.models_mixin import TimeStampedMixin


class Room(TimeStampedMixin):
    number = models.IntegerField(
        verbose_name='Номер комнаты',
        validators=[MinValueValidator(1)],
        unique=True
    )
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Стоимость')
    capacity = models.IntegerField(
        verbose_name='Вместимость',
        validators=[MinValueValidator(1)]
    )

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def __str__(self):
        return str(self.number)

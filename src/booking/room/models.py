from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from booking.utils.models_mixin import TimeStampedMixin, UUIDMixin


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

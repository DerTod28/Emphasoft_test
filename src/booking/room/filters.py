from typing import Union

import django_filters
from django.db.models import QuerySet

from booking.reservation.models import RoomReservation
from booking.room.models import Room


class DateRangeFilterSet(django_filters.FilterSet):
    """
    Filter for Room instance for searching available rooms in date range.
    """
    available = django_filters.DateFromToRangeFilter(
        method='my_custom_filter',
        label='Available dates'
    )

    class Meta:
        model = Room
        fields = ['available', 'price', 'capacity']

    def my_custom_filter(self, queryset, name, value: slice) -> Union[QuerySet, list[Room]]:
        queryset = queryset.exclude(
            reservation__start_date__lt=value.stop,
            reservation__end_date__gt=value.start,
            roomreservation__set__status=RoomReservation.StatusType.APPROVED
        )
        return queryset

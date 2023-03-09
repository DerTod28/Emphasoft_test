import django_filters
from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError

from booking.reservation.models import RoomReservation
from booking.room.models import Room


class RoomFilterSet(django_filters.FilterSet):
    """
    Filter for Room instance for searching available rooms in date range,
    filtering by price and capacity.
    """
    available = django_filters.DateFromToRangeFilter(
        method='available_filter',
        label='Available dates',
    )
    price__gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Room
        fields = ['available', 'price', 'capacity']

    def available_filter(self, queryset, name, value: slice) -> QuerySet:
        if not (value.start and value.stop):
            raise ValidationError(
                {'detail': 'available_before and available_after has to be specified.'}
            )

        if value.start.date() == value.stop.date():
            raise ValidationError(
                {'detail': 'available_before and available_after has to differ.'}
            )

        queryset = queryset.exclude(
            reservation__start_date__lt=value.stop,
            reservation__end_date__gt=value.start,
            roomreservation__status=RoomReservation.StatusType.APPROVED
        )
        return queryset

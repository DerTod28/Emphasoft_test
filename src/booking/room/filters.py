import django_filters

from booking.reservation.models import RoomReservation
from booking.room.models import Room


class DateRangeFilterSet(django_filters.FilterSet):
    available = django_filters.DateFromToRangeFilter(method='my_custom_filter', label="Свободные даты")

    class Meta:
        model = Room
        fields = ['available', 'price', 'capacity']

    def my_custom_filter(self, queryset, name, value: slice):
        queryset = queryset.exclude(
            reservation__start_date__lt=value.stop,
            reservation__end_date__gt=value.start,
            roomreservation__set__status=RoomReservation.StatusType.APPROVED
        )
        return queryset

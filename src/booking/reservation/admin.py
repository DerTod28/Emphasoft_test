from django.contrib import admin

from booking.reservation.models import Reservation, RoomReservation


class RoomReservationInline(admin.TabularInline):
    model = RoomReservation
    extra = 1


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['guest', 'start_date', 'end_date']
    search_fields = ['guest', 'start_date', 'end_date']
    raw_id_fields = ['guest', 'room']

    inlines = (RoomReservationInline,)


admin.site.register(Reservation, ReservationAdmin)


class RoomReservationAdmin(admin.ModelAdmin):
    list_display = ['reservation', 'room', 'status']
    readonly_fields = ['reservation']


admin.site.register(RoomReservation, RoomReservationAdmin)

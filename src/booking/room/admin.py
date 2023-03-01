from django.contrib import admin
from .models import Room, RoomType, Reservation, RoomReservation


class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'price', 'capacity',
                    'type', 'created']
    search_fields = ['number', 'price', 'capacity',
                     'type__name']

    ordering = ['number', 'price', 'capacity', 'type']
    raw_id_fields = ["type"]


admin.site.register(Room, RoomAdmin)


class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


admin.site.register(RoomType, RoomTypeAdmin)


class RoomReservationInline(admin.TabularInline):
    model = RoomReservation
    extra = 3


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['guest', 'start_date', 'end_date']
    search_fields = ['guest', 'start_date', 'end_date']
    raw_id_fields = ["guest", "room"]

    inlines = (RoomReservationInline,)


admin.site.register(Reservation, ReservationAdmin)


class RoomReservationAdmin(admin.ModelAdmin):
    list_display = ['reservation', 'room', 'price', 'status']


admin.site.register(RoomReservation, RoomReservationAdmin)

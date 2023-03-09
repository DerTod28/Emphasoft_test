from django.contrib import admin

from booking.room.models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'price', 'capacity', 'created']
    search_fields = ['number', 'price', 'capacity']
    ordering = ['number', 'price', 'capacity']


admin.site.register(Room, RoomAdmin)

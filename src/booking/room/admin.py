from django.contrib import admin

from .models import Room, RoomType


class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'price', 'capacity',
                    'type', 'created']
    search_fields = ['number', 'price', 'capacity',
                     'type__name']

    ordering = ['number', 'price', 'capacity', 'type']
    raw_id_fields = ['type']


admin.site.register(Room, RoomAdmin)


class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


admin.site.register(RoomType, RoomTypeAdmin)

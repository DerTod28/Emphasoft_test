from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import RoomReservation


@receiver(m2m_changed, sender=RoomReservation)
def total_price(sender, instance: RoomReservation, **kwargs):
    """
    Counting total price = room_price * days
    """
    reservation_id = instance.id

    for obj in instance.room.through.objects.all():

        if obj.reservation.id == reservation_id:
            obj.price = obj.room.price * (instance.end_date - instance.start_date).days
            obj.save()

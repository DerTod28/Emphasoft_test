from django.apps import AppConfig


class ReservationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking.reservation'

    def ready(self):
        from booking.reservation import signals

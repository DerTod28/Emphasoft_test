import uuid

from django.db import models
from rest_framework import permissions


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class PermissionsMixin(object):

    action_permissions = {}

    def get_permissions(self):
        try:
            return [permission() for permission in self.action_permissions[self.action]]
        except KeyError:
            return super().get_permissions()

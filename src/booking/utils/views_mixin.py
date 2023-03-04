
class PermissionsMixin(object):

    action_permissions = {}

    def get_permissions(self):
        try:
            return [permission() for permission in self.action_permissions[self.action]]
        except KeyError:
            return super().get_permissions()


class SerializerMixin(object):

    action_serializers = {}

    def get_serializer_class(self):
        if self.action in self.action_serializers:
            return self.action_serializers[self.action]
        return super().get_serializer_class()

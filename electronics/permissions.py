from rest_framework.permissions import BasePermission


class IsActiveStaff(BasePermission):
    """ Проверка на активность сотрудника. """

    def has_permission(self, request, view):
        """Разрешается доступ только активным сотрудникам. """
        return bool(
            request.user and request.user.is_authenticated and request.user.is_staff and request.user.is_active
        )

from rest_framework.permissions import DjangoModelPermissions


class CustomDjangoModelPermissions(DjangoModelPermissions):
    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }

    def has_permission(self, request, view):
        has_permissions = False
        if (
            request.user
            and request.user.is_authenticated
            or not self.authenticated_users_only
        ):
            queryset = self._queryset(view)
            perms = self.get_required_permissions(request.method, queryset.model)
            has_permissions = request.user.has_perms(perms)
        return has_permissions

from rest_framework.permissions import BasePermission


class GlobalDefaultPermissions(BasePermission):
    def has_permission(self, request, view):
        model_permission = self.__get_model_permission(request.method, view)
        if not model_permission:
            return False

        return request.user.has_perm(model_permission)

    def __get_model_permission(self, method, view):
        method_actions = {
            "GET": "view",
            "OPTIONS": "view",
            "HEAD": "view",
            "PUT": "change",
            "PATCH": "change",
            "POST": "add",
            "DELETE": "delete",
        }

        try:
            model_name = view.queryset.model._meta.model_name
            app_name = view.queryset.model._meta.app_label
            action_name = method_actions.get(method, "")
            return f"{app_name}.{action_name}_{model_name}"
        except AttributeError:
            return None

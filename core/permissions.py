from rest_framework import permissions


class IsInCanViewItems(permissions.BasePermission):

    def has_permission(self, request, view):
        has_permission = False
        g = request.user.groups.all()
        for i in g:
            if i.name == 'canViewItem':
                has_permission = True
        return has_permission

from rest_framework import permissions

from .permissions import IsStaffEditorPermission

class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


class UserQuerySetMixin():
    user_field = 'user'
    
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = user
        print("""⛄   \x1b[1;35;40mmixins.py:17 lookup_data:""") ## DELETEME
        print(lookup_data) ## DELETEME
        print('\x1b[0m') ## DELETEME
        qs = super().get_queryset(*args, **kwargs)
        print("""🟫   \x1b[1;36;40mmixins.py:21 qs:""") ## DELETEME
        print(qs) ## DELETEME
        print('\x1b[0m') ## DELETEME
        return qs.filter(**lookup_data)

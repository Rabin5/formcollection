from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models.user import User
from users.models.user_group import GlobalPermission

admin.site.register(User)

class GlobalPermissionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return GlobalPermission.objects.filter(content_type__model='global permission')

admin.site.register(GlobalPermission, GlobalPermissionAdmin)

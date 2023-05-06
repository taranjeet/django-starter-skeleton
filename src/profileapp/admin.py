from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    fk_name = "user"
    verbose_name_plural = "profile"
    fields = (
        "uuid",
    )
    readonly_fields = ("uuid", )
    exclude = (
        "created_at",
        "updated_at",
    )

class UserAdmin(BaseUserAdmin):
    inlines = (
        UserProfileInline,
    )
    list_display = (
        "id", "username", "email", "is_staff",
    )
    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
        "date_joined",
        "last_login",
    )
    ordering = ("-id", )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
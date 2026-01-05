from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Department, Profile, Member, ExcelFile, EmailLog
from .utils import process_pdf_and_send_emails, process_sheet_and_send_emails


# ----------------------------
# Utility Permission Check
# ----------------------------
def is_admin_user(request):
    return request.user.is_superuser or (
        hasattr(request.user, 'profile') and request.user.profile.role == 'manager'
    )


# ----------------------------
# User Admin (Profile Inline)
# ----------------------------
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    extra = 0


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

    def has_module_permission(self, request):
        return is_admin_user(request)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# ----------------------------
# Department Admin
# ----------------------------
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    def has_module_permission(self, request):
        return is_admin_user(request)


# ----------------------------
# Profile Admin
# ----------------------------
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'department')
    list_filter = ('role', 'department')

    def has_module_permission(self, request):
        return is_admin_user(request)


# ----------------------------
# Member Admin
# ----------------------------
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sheet_name', 'department', 'created_by')
    list_filter = ('department', 'sheet_name')
    search_fields = ('name', 'email')

    def has_module_permission(self, request):
        return is_admin_user(request)


# ----------------------------
# ExcelFile Admin
# ----------------------------
@admin.register(ExcelFile)
class ExcelFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'department', 'uploaded_by', 'upload_time')
    list_filter = ('department', 'upload_time')

    actions = [
        process_pdf_and_send_emails,
        process_sheet_and_send_emails
    ]

    def has_module_permission(self, request):
        return is_admin_user(request)

# ----------------------------
# Email Log Admin
# ----------------------------
@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = (
        "recipient_email",
        "sheet_name",
        "send_type",
        "status",
        "sent_by",
        "sent_at",
    )

    list_filter = (
        "send_type",
        "status",
        "sent_at",
    )

    search_fields = (
        "recipient_email",
        "sheet_name",
        "sent_by__username",
    )

    ordering = ("-sent_at",)

    readonly_fields = (
        "sent_by",
        "recipient_email",
        "sheet_name",
        "send_type",
        "status",
        "error_message",
        "sent_at",
    )

    fieldsets = (
        ("Email Info", {
            "fields": (
                "recipient_email",
                "sheet_name",
                "send_type",
                "status",
            )
        }),
        ("Sender", {
            "fields": ("sent_by",)
        }),
        ("Error Details", {
            "fields": ("error_message",)
        }),
        ("Timestamp", {
            "fields": ("sent_at",)
        }),
    )

    def has_add_permission(self, request):
        # Logs should never be added manually
        return False

    def has_change_permission(self, request, obj=None):
        # Logs should not be edited
        return False

    def has_delete_permission(self, request, obj=None):
        # Optional: allow only superadmin to delete logs
        return request.user.is_superuser

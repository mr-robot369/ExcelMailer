from django.db import models
from django.contrib.auth.models import User


# ----------------------------
# Department
# ----------------------------
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# ----------------------------
# Profile (Role Management)
# ----------------------------
class Profile(models.Model):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('head', 'Department Head'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE   # mandatory + safe
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"



# ----------------------------
# Member (Previously Teacher)
# ----------------------------
class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    sheet_name = models.CharField(
        max_length=100,
        help_text="Excel sheet name mapped to this member"
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Department head who created this member"
    )

    class Meta:
        unique_together = ('email', 'department')

    def __str__(self):
        return f"{self.name} ({self.department.name})"


# ----------------------------
# Excel Upload
# ----------------------------
class ExcelFile(models.Model):
    file = models.FileField(upload_to='excel_files/')
    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} - {self.department.name}"


class EmailLog(models.Model):
    SEND_TYPE_CHOICES = (
        ("excel", "Excel"),
        ("pdf", "PDF"),
    )

    STATUS_CHOICES = (
        ("success", "Success"),
        ("failed", "Failed"),
    )

    sent_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="email_logs"
    )
    recipient_email = models.EmailField()
    sheet_name = models.CharField(max_length=100)
    send_type = models.CharField(max_length=10, choices=SEND_TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    error_message = models.TextField(blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recipient_email} | {self.sheet_name} | {self.send_type}"
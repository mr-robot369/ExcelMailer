from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # --------------------
    # Public Pages
    # --------------------
    path('', views.home, name='home'),

    # --------------------
    # Authentication
    # --------------------
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='home'),
        name='logout'
    ),

    # --------------------
    # Department Head Dashboard (Next Steps)
    # --------------------
    path('dashboard/', views.dashboard, name='dashboard'),

    # --------------------
    # Member Management
    # --------------------
    path('members/', views.member_list, name='member_list'),
    path('members/add/', views.member_add, name='member_add'),
    path('members/delete/<int:pk>/', views.member_delete, name='member_delete'),

    # --------------------
    # Excel Management
    # --------------------
    path('excel/upload/', views.excel_upload, name='excel_upload'),
    path('excel/send/', views.excel_send, name='excel_send'),

    # --------------------
    # Email Log
    # --------------------
    path("email-logs/", views.email_logs, name="email_logs"),

    # --------------------
    # Excel file Preview
    # --------------------
    path(
        "excel/preview/<int:excel_id>/<str:sheet_name>/",
        views.excel_preview,
        name="excel_preview"
    ),

    # --------------------
    # Email Log Export
    # --------------------
    path("email-logs/export/", views.export_email_logs, name="export_email_logs"),

]

from django.urls import path
from . import admin_dashboard

urlpatterns = [
    path('admin_base',admin_dashboard.admin_base,name="admin_base"),
    path('dashboard/',admin_dashboard.dashboard,name="dashboard"),
    path('admin_properties_listout',admin_dashboard.admin_properties_listout,name="admin_properties_listout"),
    path('admin_client_details',admin_dashboard.admin_client_details,name="admin_client_details")
]

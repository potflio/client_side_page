from django.shortcuts import render,redirect
from .models import *

def admin_base(request):
    return render(request,"admin_base.html")

def dashboard(request):
    return render(request,"admin_dashboard.html")

def admin_properties_listout(request):
    return render(request,"admin_properties_listout.html")

def admin_client_details(request):
    return render(request,"admin_client_details")
from django.shortcuts import render,redirect
from .models import *


def base(request):
    request.session['is_active'] = True
    return render(request,'base.html')

def residential_properties_show(request):
    return render(request,"residential_properties_show.html")

def welcome(request):
    return render(request,"welcome.html")

def post_property(request):
    return render(request,'post_property.html')

def residential_rent_form(request):
    return render(request,"residential_rent_form.html")

def residential_resale_form(request):
    return render(request,"residential_resale_form.html")

def residential_lease_form(request):
    return render(request,"residential_lease_form.html")

def commercial_rent_form(request):
    return render(request,"commercial_rent_form.html")

def commercial_sale_form(request):
    return render(request,"commercial_sale_form.html")

def land_resale_form(request):
    return render(request,'land_resale_form.html')

def land_lease_form(request):
    return render(request,"land_lease_form.html")

def profile(request):
    email = request.session['emailId']
    context = {'email':email}
    return render(request,"profile.html",context)

def example(request):
    return render(request,"example.html")

def land_properties_view(request):
    return render(request,"land_properties_view.html")

def property_view(request):
    return render(request,"property_view.html")

def data_processing(request):
    return render(request,"data_processing.html")

def plans(request):
    return render(request,"plans.html")

def land_rent_form(request):
    return render(request,"land_rent_form.html")
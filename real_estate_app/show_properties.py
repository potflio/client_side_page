from django.shortcuts import render,redirect
from .models import *

def index(request):
    request.session['is_active'] = True
    land = Land.objects.all()[:3]
    residential = Residential.objects.all()[:3]
    # commercial = Commercial.objects.all()[:3]
    context = {'land' : land,
               'residential' : residential,
            #    'commercial' : commercial
            }
    return render(request,'index.html',context)


def land_view(request, id):
    members = Land.objects.get(id=id)
    context = {'member': members}
    return render(request, 'land_view.html', context)

def land_properties_show(request):
    land_properties = Land.objects.all()
    return render(request,'land_properties_show.html',{'land_properties':land_properties})


def property_view(request):
    property_view = LandResale.objects.all()
    return render(request,'property_view.html',{'property_view':property_view})

def residential_properties_show(request):
    residential_properties = Residential.objects.all()
    return render(request,'residential_properties_show.html',{'residential_properties':residential_properties})
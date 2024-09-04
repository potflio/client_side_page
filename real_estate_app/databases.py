from django.shortcuts import render,redirect
from .models import *

def land_rent_create(request):  
    if request.method == 'POST':
        land_rent = LandRent(
            Email = request.session['emailId'],
            Length=request.POST['Length'], 
            Width = request.POST['Width'],
            PlotArea = request.POST['PlotArea'],
            Cent = request.POST['Cent'],
            Acre = request.POST['Acre'],
            District = request.POST['District'],
            Town = request.POST['Town'],
            Street = request.POST['Street'],
            ExpectedRent = request.POST['ExpectedRent'],
            ExpectedDepositMonths = request.POST['ExpectedDepositMonths'],
            ExpectedDeposit = request.POST['ExpectedDeposit'],
            Terms = request.POST['Terms'],
            PrimaryNumber = request.POST['PrimaryNumber'],
            SecondaryNumber = request.POST['SecondaryNumber']
        )
        land = Land(
            Email = request.session['emailId'],
            Length=request.POST['Length'], 
            Width = request.POST['Width'],
            PlotArea = request.POST['PlotArea'],
            Cent = request.POST['Cent'],
            Acre = request.POST['Acre'],
            District = request.POST['District'],
            Town = request.POST['Town'],
            Street = request.POST['Street'],
            ExpectedRent = request.POST['ExpectedRent'],
            ExpectedDepositMonths = request.POST['ExpectedDepositMonths'],
            ExpectedDeposit = request.POST['ExpectedDeposit'],
            Terms = request.POST['Terms'],
            Type = 'Rent',
            PrimaryNumber = request.POST['PrimaryNumber'],
            SecondaryNumber = request.POST['SecondaryNumber']
        )
        land_rent.save()
        land.save()
        return redirect('index')
    
def land_resale_create(request):
    if request.method == 'POST':
        land_resale = LandResale(
            Email = request.session['emailId'],
            Length = request.POST['Length'], 
            Width = request.POST['Width'],
            PlotArea = request.POST['PlotArea'],
            Cent = request.POST['Cent'],
            Acre = request.POST['Acre'],
            District = request.POST['District'],
            Town = request.POST['Town'],
            Street = request.POST['Street'],
            PricePerCent = request.POST['PricePerCent'],
            TotalPrice = request.POST['TotalPrice'],
            PricePerSquareFeet = request.POST['PricePerSquareFeet'],
            Description = request.POST['Description'],
            PrimaryNumber = request.POST['PrimaryNumber'],
            SecondaryNumber = request.POST['SecondaryNumber']
        )

        land = Land(
            Email = request.session['emailId'],
            Length = request.POST['Length'], 
            Width = request.POST['Width'],
            PlotArea = request.POST['PlotArea'],
            Cent = request.POST['Cent'],
            Acre = request.POST['Acre'],
            District = request.POST['District'],
            Town = request.POST['Town'],
            Street = request.POST['Street'],
            PricePerCent = request.POST['PricePerCent'],
            TotalPrice = request.POST['TotalPrice'],
            PricePerSquareFeet = request.POST['PricePerSquareFeet'],
            Description = request.POST['Description'],
            Type = 'Resale',
            PrimaryNumber = request.POST['PrimaryNumber'],
            SecondaryNumber = request.POST['SecondaryNumber']
        )
        land_resale.save()
        land.save()
        return redirect('/')
    

def land_lease_create(request):
    if request.method == 'POST':
        land_lease = LandLease(
            Email = request.session['emailId'],
            Length=request.POST['Length'], 
            Width = request.POST['Width'],
            PlotArea = request.POST['PlotArea'],
            Cent = request.POST['Cent'],
            Acre = request.POST['Acre'],
            District = request.POST['District'],
            Town = request.POST['Town'],
            Street = request.POST['Street'],
            ExpectedLease = request.POST['ExpectedLease'],
            ExpectedLeaseDuration = request.POST['ExpectedLeaseDuration'],
            Maintenance = request.POST['Maintenance'],
            Terms = request.POST['Terms'],
            PrimaryNumber = request.POST['PrimaryNumber'],
            SecondaryNumber = request.POST['SecondaryNumber']
        )

        land = Land(
            Email = request.session['emailId'],
            Length=request.POST['Length'], 
            Width = request.POST['Width'],
            PlotArea = request.POST['PlotArea'],
            Cent = request.POST['Cent'],
            Acre = request.POST['Acre'],
            District = request.POST['District'],
            Town = request.POST['Town'],
            Street = request.POST['Street'],
            ExpectedLease = request.POST['ExpectedLease'],
            ExpectedLeaseDuration = request.POST['ExpectedLeaseDuration'],
            Maintenance = request.POST['Maintenance'],
            Terms = request.POST['Terms'],
            Type = 'Lease',
            PrimaryNumber = request.POST['PrimaryNumber'],
            SecondaryNumber = request.POST['SecondaryNumber']
        )
        land_lease.save()
        land.save()
        return redirect('/')

def residential_rent_create(request):
    if request.method == 'POST':
        residential_rent = ResidentialRent(
            Email = request.session['emailId'],
            BhkType = request.POST['BhkType'],
            Floor = request.POST['Floor'],
            HouseType = request.POST['HouseType'],
            Parking = request.POST['Parking'],
            Terrace = request.POST['Terrace'],
            Hall = request.POST['Hall'],
            Bedroom = request.POST['Bedroom'],
            Bathroom = request.POST['Bathroom'],
            District = request.POST['District'],
            Town = request.POST['Town'],
            Street = request.POST['Street'],
            ExpectedRent = request.POST['ExpectedRent'],
            ExpectedDepositMonths = request.POST['ExpectedDepositMonths'],
            ExpectedDeposit = request.POST['ExpectedDeposit'],
            Maintenance = request.POST['Maintenance'],
            PreferredTenants = request.POST['PreferredTenants'],
            Terms = request.POST['Terms'],
            PrimaryNumber = request.POST['PrimaryNumber'],
            SecondaryNumber = request.POST['SecondaryNumber']
        )
        residential = Residential(
            Email = request.session['emailId'],
            BhkType = request.POST['BhkType'],
            Floor = request.POST['Floor'],
            HouseType = request.POST['HouseType'],
            Parking = request.POST['Parking'],
            Terrace = request.POST['Terrace'],
            Hall = request.POST['Hall'],
            Bedroom = request.POST['Bedroom'],
            Bathroom = request.POST['Bathroom'],
            District = request.POST['District'],
            Town = request.POST['Town'],
            Street = request.POST['Street'],
            ExpectedRent = request.POST['ExpectedRent'],
            ExpectedDepositMonths = request.POST['ExpectedDepositMonths'],
            ExpectedDeposit = request.POST['ExpectedDeposit'],
            Maintenance = request.POST['Maintenance'],
            PreferredTenants = request.POST['PreferredTenants'],
            Terms = request.POST['Terms'],
            Type = 'Rent',
            PrimaryNumber = request.POST['PrimaryNumber'],
            SecondaryNumber = request.POST['SecondaryNumber']
        )
        residential.save()
        residential_rent.save()
        return redirect('/')
    

def residential_resale_create(request):
    if request.method == 'POST':
        residential_resale = ResidentialResale(
            Email = request.session['emailId'],
            BhkType = request.POST['BhkType'],
            TotalFloor = request.POST['TotalFloor'],
            PropertyAge = request.POST['PropertyAge'],
            HouseLength = request.POST['HouseLength'],
            HouseWidth = request.POST['HouseWidth'],
            HousePlotArea = request.POST['HousePlotArea'],
            HouseCent = request.POST['HouseCent'],
            LandLength = request.POST['LandLength'],
            LandWidth = request.POST['LandWidth'],
            LandPlotArea = request.POST['LandPlotArea'],
            LandCent = request.POST['LandCent'],
            Parking = request.POST['Parking'],
            Terrace = request.POST['Terrace'],
            Hall = request.POST['Hall'],
            Bedroom = request.POST['Bedroom'],
            Bathroom = request.POST['Bathroom'],
            District = request.POST['District'],
            Town = request.POST['Town'],
            Street = request.POST['Street'],
            ExpectedPrice = request.POST['ExpectedPrice'],
            Description = request.POST['Description'],        
            PrimaryNumber = request.POST['PrimaryNumber'],
            SecondaryNumber = request.POST['SecondaryNumber']
        )
        residential = Residential(
            Email = request.session['emailId'],
            BhkType = request.POST['BhkType'],
            TotalFloor = request.POST['TotalFloor'],
            PropertyAge = request.POST['PropertyAge'],
            HouseLength = request.POST['HouseLength'],
            HouseWidth = request.POST['HouseWidth'],
            HousePlotArea = request.POST['HousePlotArea'],
            HouseCent = request.POST['HouseCent'],
            LandLength = request.POST['LandLength'],
            LandWidth = request.POST['LandWidth'],
            LandPlotArea = request.POST['LandPlotArea'],
            LandCent = request.POST['LandCent'],
            Parking = request.POST['Parking'],
            Terrace = request.POST['Terrace'],
            Hall = request.POST['Hall'],
            Bedroom = request.POST['Bedroom'],
            Bathroom = request.POST['Bathroom'],
            District = request.POST['District'],
            Town = request.POST['Town'],
            Street = request.POST['Street'],
            ExpectedPrice = request.POST['ExpectedPrice'],
            Description = request.POST['Description'],  
            Type = 'Resale',      
            PrimaryNumber = request.POST['PrimaryNumber'],
            SecondaryNumber = request.POST['SecondaryNumber']
        )
        residential.save()
        residential_resale.save()
        return redirect('/')

def residential_lease_create(request):
    if request.method == "POST":
        residential_lease = ResidentialLease(
            Email = request.session['emailId'],
            BhkType = request.POST['BhkType'],
            Floor = request.POST['Floor'],
            HouseType = request.POST['HouseType'],
            Parking = request.POST['Parking'],
            Terrace = request.POST['Terrace'],
            Hall = request.POST['Hall'],
            Bedroom = request.POST['Bedroom'],
            Bathroom = request.POST['Bathroom'],
            District = request.POST['District'],
            Town = request.POST['Town'],
            Street = request.POST['Street'],
            ExpectedLease = request.POST['ExpectedLease'],
            ExpectedLeaseDuration = request.POST['ExpectedLeaseDuration'],
            Maintenance = request.POST['Maintenance'],
            Terms = request.POST['Terms'],
            PrimaryNumber = request.POST['PrimaryNumber'],
            SecondaryNumber = request.POST['SecondaryNumber']
        )
        residential = Residential(
            Email = request.session['emailId'],
            BhkType = request.POST['BhkType'],
            Floor = request.POST['Floor'],
            HouseType = request.POST['HouseType'],
            Parking = request.POST['Parking'],
            Terrace = request.POST['Terrace'],
            Hall = request.POST['Hall'],
            Bedroom = request.POST['Bedroom'],
            Bathroom = request.POST['Bathroom'],
            District = request.POST['District'],
            Town = request.POST['Town'],
            Street = request.POST['Street'],
            ExpectedLease = request.POST['ExpectedLease'],
            ExpectedLeaseDuration = request.POST['ExpectedLeaseDuration'],
            Maintenance = request.POST['Maintenance'],
            Type = 'Lease',
            Terms = request.POST['Terms'],
            PrimaryNumber = request.POST['PrimaryNumber'],
            SecondaryNumber = request.POST['SecondaryNumber']
        )
        residential.save()
        residential_lease.save()
        return redirect('/')

def email_login(request):
    login = LoginDetails(
        email = request.POST['email'],
        otp = request.POST['otp']
    )
    login.save()
    return redirect('/')

def display_data(request):
    # Fetch data from MySQL database
    records = LandResale.objects.all()

    # Render the template with data
    return render(request, 'data_display.html', {'records': records}) 
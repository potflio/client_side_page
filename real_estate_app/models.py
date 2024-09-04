from django.db import models
from django.core.validators import EmailValidator
from django.utils import timezone


class Land(models.Model):
    Email = models.EmailField(validators=[EmailValidator()], unique=False)
    Length = models.DecimalField(max_digits=10, decimal_places=2)  
    Width = models.DecimalField(max_digits=10, decimal_places=2)  
    PlotArea = models.DecimalField(max_digits=10,decimal_places=2) 
    Cent = models.DecimalField(max_digits=10,decimal_places=2)
    Acre = models.DecimalField(max_digits=10,decimal_places=2)
    District = models.CharField(max_length=50)
    Town = models.CharField(max_length=50)
    Street = models.CharField(max_length=50)
    ExpectedRent = models.IntegerField(default='0')
    ExpectedDepositMonths = models.CharField(max_length=20,default='0')
    ExpectedDeposit = models.IntegerField(default='0')
    PricePerCent = models.DecimalField(max_digits=10, decimal_places=2,default='0') 
    TotalPrice = models.DecimalField(max_digits=10, decimal_places=2,default='0')
    PricePerSquareFeet = models.DecimalField(max_digits=10, decimal_places=2,default='0') 
    ExpectedLease = models.DecimalField(max_digits=10, decimal_places=2,default='0')  
    ExpectedLeaseDuration = models.CharField(max_length=12,default='-')
    Maintenance = models.CharField(max_length=20,default='-')
    Description = models.CharField(max_length=500,default='-')
    Terms = models.CharField(max_length=500,default='-')
    Type = models.CharField(max_length=10)
    PrimaryNumber = models.CharField(max_length=20, unique=False)
    SecondaryNumber = models.CharField(max_length=20, unique=False)
    Uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "land_records"

class LandRent(models.Model):
    Email = models.EmailField(validators=[EmailValidator()], unique=False)
    Length = models.DecimalField(max_digits=10, decimal_places=2)  # Example: 10.5
    Width = models.DecimalField(max_digits=10, decimal_places=2)   # Example: 20.25
    PlotArea = models.DecimalField(max_digits=10,decimal_places=2)  # Example: '100 sq. ft.'
    Cent = models.DecimalField(max_digits=10,decimal_places=2)
    Acre = models.DecimalField(max_digits=10,decimal_places=2)
    District = models.CharField(max_length=50)
    Town = models.CharField(max_length=50)
    Street = models.CharField(max_length=50)
    ExpectedRent = models.IntegerField()  # Example: 50000.00
    ExpectedDepositMonths = models.CharField(max_length=20)
    ExpectedDeposit = models.IntegerField()
    Terms = models.CharField(max_length=500)
    PrimaryNumber = models.CharField(max_length=20, unique=False)
    SecondaryNumber = models.CharField(max_length=20, unique=False)
    Uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "land_rent"

class LandResale(models.Model):
    Email = models.EmailField(validators=[EmailValidator()], unique=False)
    Length = models.DecimalField(max_digits=10, decimal_places=2)  # Example: 10.5
    Width = models.DecimalField(max_digits=10, decimal_places=2)   # Example: 20.25
    PlotArea = models.DecimalField(max_digits=10,decimal_places=2)  # Example: '100 sq. ft.'
    Cent = models.DecimalField(max_digits=10,decimal_places=2)
    Acre = models.DecimalField(max_digits=10,decimal_places=2)
    District = models.CharField(max_length=50)
    Town = models.CharField(max_length=50)
    Street = models.CharField(max_length=50)
    PricePerCent = models.DecimalField(max_digits=10, decimal_places=2)  # Example: 50000.00
    TotalPrice = models.DecimalField(max_digits=15, decimal_places=2)
    PricePerSquareFeet = models.DecimalField(max_digits=10, decimal_places=2)  # Example: 50000.00
    Description = models.CharField(max_length=500)
    PrimaryNumber = models.CharField(max_length=20, unique=False)
    SecondaryNumber = models.CharField(max_length=20, unique=False)
    Uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "land_resale"

class LandLease(models.Model):
    Email = models.EmailField(validators=[EmailValidator()], unique=False)
    Length = models.DecimalField(max_digits=10, decimal_places=2)  # Example: 10.5
    Width = models.DecimalField(max_digits=10, decimal_places=2)   # Example: 20.25
    PlotArea = models.DecimalField(max_digits=10,decimal_places=2)  # Example: '100 sq. ft.'
    Cent = models.DecimalField(max_digits=10,decimal_places=2)
    Acre = models.DecimalField(max_digits=10,decimal_places=2)
    District = models.CharField(max_length=50)
    Town = models.CharField(max_length=50)
    Street = models.CharField(max_length=50)
    ExpectedLease = models.IntegerField()  # Example: 50000.00
    ExpectedLeaseDuration = models.CharField(max_length=12)
    Maintenance = models.CharField(max_length=20)
    Terms = models.CharField(max_length=500)
    PrimaryNumber = models.CharField(max_length=20, unique=False)
    SecondaryNumber = models.CharField(max_length=20, unique=False)
    Uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "land_lease"

class Residential(models.Model):
    BhkType = models.CharField(max_length=50)
    Email = models.EmailField(validators=[EmailValidator()], unique=False)
    Floor = models.CharField(max_length=50,default='-')
    HouseType = models.CharField(max_length=20,default='-')
    Parking = models.CharField(max_length=50)
    Terrace = models.CharField(max_length=50)
    Hall = models.CharField(max_length=50)
    Bedroom = models.CharField(max_length=50)
    Bathroom = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    Town = models.CharField(max_length=50)
    Street = models.CharField(max_length=50)
    ExpectedRent = models.IntegerField(default='0')
    ExpectedDepositMonths = models.IntegerField(default='0')
    ExpectedDeposit = models.IntegerField(default='0')
    PreferredTenants = models.CharField(max_length=50,default='-')
    TotalFloor = models.CharField(max_length=50,default='-')
    PropertyAge = models.CharField(max_length=50,default='-')
    HouseLength = models.DecimalField(max_digits=10,decimal_places=2,default='0')
    HouseWidth = models.DecimalField(max_digits=10,decimal_places=2,default='0')
    HousePlotArea = models.DecimalField(max_digits=10,decimal_places=2,default='0')
    HouseCent = models.DecimalField(max_digits=10,decimal_places=2,default='0')
    LandLength = models.DecimalField(max_digits=10,decimal_places=2,default='0')
    LandWidth = models.DecimalField(max_digits=10,decimal_places=2,default='0')
    LandPlotArea = models.DecimalField(max_digits=10,decimal_places=2,default='0')
    LandCent = models.DecimalField(max_digits=10,decimal_places=2,default='0')
    ExpectedPrice = models.IntegerField(default='0')
    Description = models.CharField(max_length=50,default='-')
    ExpectedLease = models.IntegerField(default='0')
    ExpectedLeaseDuration = models.CharField(max_length=50,default='-')
    Maintenance = models.CharField(max_length=50,default='-')
    Terms = models.CharField(max_length=1000,default='-')
    Type = models.CharField(max_length=10)
    PrimaryNumber = models.CharField(max_length=20, unique=False)
    SecondaryNumber = models.CharField(max_length=20, unique=False)
    Created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = "residential_records"

class ResidentialRent(models.Model):
    BhkType = models.CharField(max_length=50)
    Email = models.EmailField(validators=[EmailValidator()], unique=False)
    Floor = models.CharField(max_length=50)
    HouseType = models.CharField(max_length=30)
    Parking = models.CharField(max_length=50)
    Terrace = models.CharField(max_length=50)
    Hall = models.CharField(max_length=50)
    Bedroom = models.CharField(max_length=50)
    Bathroom = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    Town = models.CharField(max_length=50)
    Street = models.CharField(max_length=50)
    ExpectedRent = models.IntegerField()
    ExpectedDepositMonths = models.IntegerField()
    ExpectedDeposit = models.IntegerField()
    Maintenance = models.CharField(max_length=50)
    PreferredTenants = models.CharField(max_length=50)
    Terms = models.CharField(max_length=1000)
    PrimaryNumber = models.CharField(max_length=20, unique=False)
    SecondaryNumber = models.CharField(max_length=20, unique=False)
    Created_at = models.DateTimeField(default=timezone.now)
    

    class Meta:
        db_table = "residential_rent"




class ResidentialResale(models.Model):
    BhkType = models.CharField(max_length=50)
    Email = models.EmailField(validators=[EmailValidator()], unique=False)
    TotalFloor = models.CharField(max_length=50)
    PropertyAge = models.CharField(max_length=50)
    HouseLength = models.FloatField()
    HouseWidth = models.FloatField()
    HousePlotArea = models.FloatField()
    HouseCent = models.FloatField()
    LandLength = models.FloatField()
    LandWidth = models.FloatField()
    LandPlotArea = models.FloatField()
    LandCent = models.FloatField()
    Parking = models.CharField(max_length=50)
    Terrace = models.CharField(max_length=50)
    Hall = models.CharField(max_length=50)
    Bedroom = models.CharField(max_length=50)
    Bathroom = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    Town = models.CharField(max_length=50)
    Street = models.CharField(max_length=50)
    ExpectedPrice = models.IntegerField()
    Description = models.CharField(max_length=50)
    PrimaryNumber = models.CharField(max_length=20, unique=False)
    SecondaryNumber = models.CharField(max_length=20, unique=False)
    Created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "residential_resale"

class ResidentialLease(models.Model):
    BhkType = models.CharField(max_length=50)
    Email = models.EmailField(validators=[EmailValidator()], unique=False)
    Floor = models.CharField(max_length=50)
    HouseType = models.CharField(max_length=50)
    Parking = models.CharField(max_length=50)
    Terrace = models.CharField(max_length=50)
    Hall = models.CharField(max_length=50)
    Bedroom = models.CharField(max_length=50)
    Bathroom = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    Town = models.CharField(max_length=50)
    Street = models.CharField(max_length=50)
    ExpectedLease = models.IntegerField()
    ExpectedLeaseDuration = models.CharField(max_length=50)
    Maintenance = models.CharField(max_length=50)
    Terms = models.CharField(max_length=1000)
    PrimaryNumber = models.CharField(max_length=20, unique=False)
    SecondaryNumber = models.CharField(max_length=20, unique=False)
    Created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = "residential_lease"

class CommercialRent(models.Model):
    class Meta:
        db_table = "commercial_rent"

class CommercialResale(models.Model):
    class Meta:
        db_table = "commercial_resale"

class LoginDetails(models.Model):
    Email = models.EmailField(validators=[EmailValidator()], unique=False)
    Otp = models.CharField(max_length=6)  # Assuming OTP length is 6 digits
    Created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "login_details"
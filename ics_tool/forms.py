from django import forms
from django.conf import settings
from .models import *

class CustomerForm(forms.ModelForm):
    CustomerId    = forms.IntegerField()
    CustomerName  = forms.CharField(max_length=10)

    class Meta:
        model = Customer
        fields = '__all__'

class AddDonorForm(forms.ModelForm):
    OrganizationName    = forms.CharField(max_length=100)
    Salutation          = forms.CharField(max_length=100)
    FirstName           = forms.CharField(max_length=100)
    LastName            = forms.CharField(max_length=100)
    Email               = forms.EmailField(max_length=100)
    PhoneNumber         = forms.CharField(max_length=15)
    Comments            = forms.CharField(max_length=100,required=False)
    StreetAddress       = forms.CharField(max_length=100)
    City                = forms.CharField(max_length=100)
    State               = forms.CharField(max_length=100)
    Zip                 = forms.CharField(max_length=100)
    ICS                 = forms.CharField(max_length=2,required=False)

    class Meta:
        model = Donors
        fields = '__all__'

class EditDonorForm(forms.ModelForm):
    SearchQuery = forms.CharField(max_length=255)

    class Meta:
        model = Donors
        fields = '__all__'
        
class AddDonationsForm(forms.ModelForm):
    SelectDonor     = forms.CharField(max_length=100)
    FirstName       = forms.CharField(max_length=100)
    LastName        = forms.CharField(max_length=100)
    DonorID         = forms.IntegerField()
    OrganizationName= forms.CharField(max_length=100)
    StreetAddress   = forms.CharField(max_length=100)
    City            = forms.CharField(max_length=100)
    State           = forms.CharField(max_length=100)
    Zip             = forms.CharField(max_length=100)
    PhoneNumber     = forms.CharField(max_length=15)
    Email           = forms.EmailField(max_length=100)
    Comments        = forms.CharField(max_length=100)
    DonationDate    = forms.CharField(max_length=100)
    TotalPounds     = forms.IntegerField()
    PurchasedbyICS  = forms.BooleanField(max_length=2,required=False)
    DonationComments= forms.CharField(max_length=100)
    Category        = forms.CharField(max_length=100)
    Pounds          = forms.IntegerField()
    

    class Meta:
        model = Donors
        fields = '__all__'
        
class SearchDonorForm(forms.ModelForm):
    SearchQuery = forms.CharField(max_length=255)

    class Meta:
        model = SearchDonor
        fields = '__all__'
        

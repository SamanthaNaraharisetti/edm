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
    Comments            = forms.CharField(max_length=225,required=False)
    StreetAddress       = forms.CharField(max_length=100)
    City                = forms.CharField(max_length=100)
    State               = forms.CharField(max_length=100)
    Zip                 = forms.CharField(max_length=100)
    DonorInactive       = forms.CharField(max_length=2,required=False)
    SearchName          = forms.CharField(max_length=100)

    class Meta:
        model = Donors
        fields = '__all__'

class AddUsers(forms.ModelForm):
    InactiveCheckBox    = forms.CharField(max_length=2,required=False)
    UserID              = forms.IntegerField()
    FirstName           = forms.CharField(max_length=100)
    LastName            = forms.CharField(max_length=100)
    UserType            = forms.CharField(max_length=100)
    UserPassword        = forms.CharField(max_length=25)
    UserComments        = forms.CharField(max_length=225)
    
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
    Comments        = forms.CharField(max_length=225)
    DonationDate    = forms.DateField(max_length=100)
    TotalPounds     = forms.IntegerField()
    PurchasedbyICS  = forms.BooleanField(max_length=2,required=False)
    DonationComments= forms.CharField(max_length=225)
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
        
class EditDonationCategories(forms.ModelForm):
    IfEdit          = forms.CharField(max_length=2,required=False)
    GrocerySortOrder = forms.IntegerField()
    GroceryCategory = forms.CharField(max_length=100)
    GroceryDescription = forms.CharField(max_length=100)
    GroceryInactiveCheckBox = forms.BooleanField(max_length=2,required=False)
    
    class Meta:
        model = Donors
        fields = '__all__'

class EditDonationsForm(forms.ModelForm):
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
    Comments        = forms.CharField(max_length=225)
    DonationID      = forms.IntegerField()
    DonationDate    = forms.CharField(max_length=100)
    TotalPounds     = forms.IntegerField()
    PurchasedbyICS  = forms.BooleanField(max_length=2,required=False)
    DonationComments= forms.CharField(max_length=225)
    Category        = forms.CharField(max_length=100)
    Pounds          = forms.IntegerField()
    Inactived       = forms.BooleanField(max_length=2,required=False)
    Lastmodified    = forms.CharField(max_length=100)
    

    class Meta:
        model = Donors
        fields = '__all__'

class EditDonationsDatasetForm(forms.ModelForm):
    From            = forms.CharField(max_length=100)
    To              = forms.CharField(max_length=100)
    AllDates        = forms.BooleanField(max_length=2,required=False)
    Inactive        = forms.BooleanField(max_length=2,required=False)
    Active          = forms.BooleanField(max_length=2,required=False)
    AllRecords      = forms.BooleanField(max_length=2,required=False)
    Donor           = forms.CharField(max_length=100)
    AllDonors       = forms.BooleanField(max_length=2,required=False)
    

    class Meta:
        model = Donors
        fields = '__all__'

class EditDonorForm(forms.ModelForm):
    SelectDonor         = forms.CharField(max_length=100)
    OrganizationName    = forms.CharField(max_length=100)
    Salutation          = forms.CharField(max_length=100)
    FirstName           = forms.CharField(max_length=100)
    LastName            = forms.CharField(max_length=100)
    Email               = forms.EmailField(max_length=100)
    PhoneNumber         = forms.CharField(max_length=15)
    Comments            = forms.CharField(max_length=225,required=False)
    StreetAddress       = forms.CharField(max_length=100)
    City                = forms.CharField(max_length=100)
    State               = forms.CharField(max_length=100)
    Zip                 = forms.CharField(max_length=100)
    DonorInactive       = forms.CharField(max_length=2,required=False)
    SearchName          = forms.CharField(max_length=100)

    class Meta:
        model = Donors
        fields = '__all__'

 class EditUsers(forms.ModelForm):
    selectUserID        = forms.CharField(max_length=100)
    InactiveCheckBox    = forms.CharField(max_length=2,required=False)
    UserID              = forms.IntegerField()
    FirstName           = forms.CharField(max_length=100)
    LastName            = forms.CharField(max_length=100)
    UserType            = forms.CharField(max_length=100)
    UserPassword        = forms.CharField(max_length=25)
    UserComments        = forms.CharField(max_length=225)
    
    class Meta:
        model = Donors
        fields = '__all__'

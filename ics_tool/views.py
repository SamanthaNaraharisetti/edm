# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render_to_response, render
from django.core.urlresolvers import reverse
from django.template import Context
import datetime
from django.http import HttpResponse
import re

from .forms import *
from .models import *


def health(request):
    return HttpResponse("3")

#@login_required(login_url="login/")
def index(request):
    template_name = 'ics_tool/home.html'

    if request.method == "GET":
        return render(request, template_name)

    form = SearchDataForm(request.POST)
    if form.is_valid():

      results = 'Welcome'

      return render(request,'ics_tool/home.html',{'Results' : results})

    print(form.errors)

    return render(request,'ics_tool/home.html',{})

def add_donor(request):
    template_name = 'ics_tool/add_donor.html'

    if request.method == "GET":
        return render(request, template_name)

    form = AddDonorForm(request.POST)
    if form.is_valid():
      OrganizationName = request.POST.get('OrganizationName', '')
      Salutation       = request.POST.get('Salutation', '')
      FirstName        = request.POST.get('FirstName', '')
      LastName         = request.POST.get('LastName', '')
      Email            = request.POST.get('Email', '')
      PhoneNumber      = request.POST.get('PhoneNumber', '')
      Comments         = request.POST.get('Comments', '')
      StreetAddress    = request.POST.get('StreetAddress', '')
      City             = request.POST.get('City', '')
      State            = request.POST.get('State', '')
      Zip              = request.POST.get('Zip', '')
      DonorInactive    = request.POST.get('DonorInactive', '')
      SearchName       = request.POST.get('SearchName', '')
    
      LoadDonorObj = Donors(OrganizationName=OrganizationName,Salutation=Salutation,FirstName=FirstName,LastName=LastName,
                            Email=Email,PhoneNumber=PhoneNumber,Comments=Comments,StreetAddress=StreetAddress,City=City,State=State,
                            Zip=Zip,DonorInactive=DonorInactive,SearchName=SearchName)
      LoadDonorObj.save()

      return render(request,'ics_tool/donor_success.html',{})

    print(form.errors)

    return render(request,'ics_tool/add_donor.html',{})

def search_donor(request):

    template_name = 'ics_tool/search_donor.html'

    if request.method == "GET":
        return render(request, template_name)

    form = SearchDonorForm(request.POST)
    if form.is_valid():
      SearchQuery = request.POST.get('SearchQuery', '')

      results = Donors.objects.filter(Q(FirstName__icontains=SearchQuery)).values()

      return render(request,'ics_tool/donor_results.html',{'Results' : results})

    print(form.errors)

    return render(request,'ics_tool/search_donor.html',{})


def add_donation(request):
    template_name = 'ics_tool/add_donations.html'

    if request.method == "GET":
        return render(request, template_name)

    form = AddDonationsForm(request.POST)
    if form.is_valid():
        SelectDonor     = request.POST.get('SelectDonor', '')
        FirstName       = request.POST.get('FirstName', '')
        LastName        = request.POST.get('LastName', '')
        DonorID         = request.POST.get('DonorID', '')
        OrganizationName= request.POST.get('OrganizationName', '')
        StreetAddress   = request.POST.get('StreetAddress', '')
        City            = request.POST.get('City', '')
        State           = request.POST.get('State', '')
        Zip             = request.POST.get('Zip', '')
        PhoneNumber     = request.POST.get('PhoneNumber', '')
        Email           = request.POST.get('Email', '')
        Comments        = request.POST.get('Comments', '')
        DonationDate    = request.POST.get('DonationDate', '')
        TotalPounds     = request.POST.get('TotalPounds', '')
        PurchasedbyICS  = request.POST.get('PurchasedbyICS', '')
        DonationComments= request.POST.get('DonationComments', '')
        Category        = request.POST.get('Category', '')
        Pounds          = request.POST.get('Pounds', '')
        
      LoadDonorObj = Donors(SelectDonor=SelectDonor,DonorID=DonorID,OrganizationName=OrganizationName,Salutation=Salutation,FirstName=FirstName,LastName=LastName,
                            Email=Email,PhoneNumber=PhoneNumber,Comments=Comments,StreetAddress=StreetAddress,City=City,State=State,Zip=Zip,DonationDate=DonationDate,
                            TotalPounds=TotalPounds,PurchasedbyICS=PurchasedbyICS,DonationComments=DonationComments,Category=Category,
                           Pounds=Pounds)
      LoadDonorObj.save()

      return render(request,'ics_tool/donor_success.html',{})

    print(form.errors)

    return render(request,'ics_tool/add_donations.html',{})

def add_users(request):
    template_name = 'ics_tool/add_users.html'

    if request.method == "GET":
        return render(request, template_name)

    form = AddUsers(request.POST)
    if form.is_valid():
      InactiveCheckBox = request.POST.get('InactiveCheckBox', '')
      UserID           = request.POST.get('UserID', '')
      FirstName        = request.POST.get('FirstName', '')
      LastName         = request.POST.get('LastName', '')
      UserType         = request.POST.get('UserType', '')
      UserPassword     = request.POST.get('UserPassword', '')
      UserComments     = request.POST.get('UserComments', '')
    
      LoadDonorObj = Donors(InactiveCheckBox=InactiveCheckBox,UserID=UserID,FirstName=FirstName,LastName=LastName,
                            UserType=UserType,UserPassword=UserPassword,UserComments=UserComments)
      LoadDonorObj.save()

      return render(request,'ics_tool/donor_success.html',{})

    print(form.errors)

    return render(request,'ics_tool/add_users.html',{})

def edit_donationCategories(request):
    template_name = 'ics_tool/edit_donationCategories.html'

    if request.method == "GET":
        return render(request, template_name)

    form = EditDonationCategories(request.POST)
    if form.is_valid():
      IfEdit = request.POST.get('IfEdit', '')
      GrocerySortOrder     = request.POST.get('GrocerySortOrder', '')
      GroceryCategory      = request.POST.get('GroceryCategory', '')
      GroceryDescription   = request.POST.get('GroceryDescription', '')
      GroceryInactiveCheckBox = request.POST.get('GroceryInactiveCheckBox', '')
      UserPassword         = request.POST.get('UserPassword', '')
      UserComments         = request.POST.get('UserComments', '')
    
      LoadDonorObj = Donors(IfEdit=IfEdit,GrocerySortOrder=GrocerySortOrder,GroceryCategory=GroceryCategory,GroceryDescription=GroceryDescription,
                            GroceryInactiveCheckBox=GroceryInactiveCheckBox)
      LoadDonorObj.save()

      return render(request,'ics_tool/donor_success.html',{})

    print(form.errors)

    return render(request,'ics_tool/edit_donationCategories.html',{})

def edit_donations(request):
    template_name = 'ics_tool/edit_donations.html'

    if request.method == "GET":
        return render(request, template_name)

    form = EditDonationsForm(request.POST)
    if form.is_valid():
        SelectDonor     = request.POST.get('SelectDonor', '')
        FirstName       = request.POST.get('FirstName', '')
        LastName        = request.POST.get('LastName', '')
        DonorID         = request.POST.get('DonorID', '')
        OrganizationName= request.POST.get('OrganizationName', '')
        StreetAddress   = request.POST.get('StreetAddress', '')
        City            = request.POST.get('City', '')
        State           = request.POST.get('State', '')
        Zip             = request.POST.get('Zip', '')
        PhoneNumber     = request.POST.get('PhoneNumber', '')
        Email           = request.POST.get('Email', '')
        Comments        = request.POST.get('Comments', '')
        DonationDate    = request.POST.get('DonationDate', '')
        TotalPounds     = request.POST.get('TotalPounds', '')
        PurchasedbyICS  = request.POST.get('PurchasedbyICS', '')
        DonationComments= request.POST.get('DonationComments', '')
        Category        = request.POST.get('Category', '')
        Pounds          = request.POST.get('Pounds', '')
        DonationID      = request.POST.get('DonationID', '')
        Inactived       = request.POST.get('Inactived', '')
        Lastmodified    = request.POST.get('Lastmodified', '')
        
      LoadDonorObj = Donors(SelectDonor=SelectDonor,DonorID=DonorID,OrganizationName=OrganizationName,Salutation=Salutation,FirstName=FirstName,LastName=LastName,
                            Email=Email,PhoneNumber=PhoneNumber,Comments=Comments,StreetAddress=StreetAddress,City=City,State=State,Zip=Zip,DonationDate=DonationDate,
                            TotalPounds=TotalPounds,PurchasedbyICS=PurchasedbyICS,DonationComments=DonationComments,Category=Category,
                           Pounds=Pounds,DonationID=DonationID,Inactived=Inactived,Lastmodified=Lastmodified)
      LoadDonorObj.save()

      return render(request,'ics_tool/donor_success.html',{})

    print(form.errors)

    return render(request,'ics_tool/edit_donations.html',{})

def edit_donations_dataset(request):
    template_name = 'ics_tool/edit_donations_dataset.html'

    if request.method == "GET":
        return render(request, template_name)

    form = EditDonationsDatasetForm(request.POST)
    if form.is_valid():
      From      = request.POST.get('From', '')
      To        = To.POST.get('To', '')
      AllDates  = request.POST.get('AllDates', '')
      Inactive  = request.POST.get('Inactive', '')
      Active    = request.POST.get('Active', '')
      AllRecords= request.POST.get('AllRecords', '')
      Donor     = request.POST.get('Donor', '')
      AllDonors = request.POST.get('AllDonors', '')
    
      LoadDonorObj = Donors(From=From,To=To,AllDates=AllDates,Inactive=Inactive,
                            Active=Active,AllRecords=AllRecords,Donor=Donor,AllDonors=AllDonors)
      LoadDonorObj.save()

      return render(request,'ics_tool/donor_success.html',{})

    print(form.errors)

    return render(request,'ics_tool/edit_donations_dataset.html',{})

def edit_donor(request):
    template_name = 'ics_tool/edit_donor.html'

    if request.method == "GET":
        return render(request, template_name)

    form = EditDonorForm(request.POST)
    if form.is_valid():
      OrganizationName = request.POST.get('OrganizationName', '')
      Salutation       = request.POST.get('Salutation', '')
      FirstName        = request.POST.get('FirstName', '')
      LastName         = request.POST.get('LastName', '')
      Email            = request.POST.get('Email', '')
      PhoneNumber      = request.POST.get('PhoneNumber', '')
      Comments         = request.POST.get('Comments', '')
      StreetAddress    = request.POST.get('StreetAddress', '')
      City             = request.POST.get('City', '')
      State            = request.POST.get('State', '')
      Zip              = request.POST.get('Zip', '')
      DonorInactive    = request.POST.get('DonorInactive', '')
      SearchName       = request.POST.get('SearchName', '')
      SelectDonor      = request.POST.get('SelectDonor', '')      
        
      LoadDonorObj = Donors(OrganizationName=OrganizationName,Salutation=Salutation,FirstName=FirstName,LastName=LastName,
                            Email=Email,PhoneNumber=PhoneNumber,Comments=Comments,StreetAddress=StreetAddress,City=City,State=State,
                            Zip=Zip,DonorInactive=DonorInactive,SearchName=SearchName,SelectDonor=SelectDonor)
      LoadDonorObj.save()

      return render(request,'ics_tool/donor_success.html',{})

    print(form.errors)

    return render(request,'ics_tool/edit_donor.html',{})

def edit_users(request):
    template_name = 'ics_tool/edit_users.html'

    if request.method == "GET":
        return render(request, template_name)

    form = EditUsers(request.POST)
    if form.is_valid():
      InactiveCheckBox = request.POST.get('InactiveCheckBox', '')
      UserID           = request.POST.get('UserID', '')
      FirstName        = request.POST.get('FirstName', '')
      LastName         = request.POST.get('LastName', '')
      UserType         = request.POST.get('UserType', '')
      UserPassword     = request.POST.get('UserPassword', '')
      UserComments     = request.POST.get('UserComments', '')
      selectUserID     = request.POST.get('selectUserID', '')
        
      LoadDonorObj = Donors(InactiveCheckBox=InactiveCheckBox,UserID=UserID,FirstName=FirstName,LastName=LastName,
                            UserType=UserType,UserPassword=UserPassword,UserComments=UserComments,selectUserID=selectUserID)
      LoadDonorObj.save()

      return render(request,'ics_tool/donor_success.html',{})

    print(form.errors)

    return render(request,'ics_tool/edit_users.html',{})

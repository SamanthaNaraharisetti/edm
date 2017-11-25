# -*- coding: utf-8 -*-
	from __future__ import unicode_literals
	

	from django.db import models
	

	# Create your models here.
	# Database Tables should be defined as class object
	class Customer(models.Model):
	    CustomerId          = models.IntegerField(max_length=20,primary_key=True)
	    CustomerFirstName   = models.CharField(max_length=200)
	    CustomerLastName    = models.CharField(max_length=200)
	    Street= models.CharField(max_length=200)
	    City= models.CharField(max_length=200)
	    State= models.CharField(max_length=200)
	    Zip=models.IntegerField(max_length=10)
	

	class Donors(models.Model):
	    OrganizationName    = models.CharField(max_length=100)
	    Salutation          = models.CharField(max_length=100)
	    FirstName           = models.CharField(max_length=100)
	    LastName            = models.CharField(max_length=100)
	    Email               = models.EmailField(max_length=100)
	    PhoneNumber         = models.CharField(max_length=15)
	    Comments            = models.CharField(max_length=100)
	    StreetAddress       = models.CharField(max_length=100)
	    City                = models.CharField(max_length=100)
	    State               = models.CharField(max_length=100)
	    Zip                 = models.CharField(max_length=100)
	    isPurchased_by_ICS  = models.BooleanField(default=False)
	  
	class DonationsLog(models.Model):
	    logID= models.IntegerField(max_length=20,primary_key=True)
	    lastModifidDate=models.DateField()
	    lastChangedBy=models.CharField(max_length=100)
	

	

	class SearchDonor(models.Model):
	    donorID =models.ForeignKey(Donors, on_delete=models.CASCADE,primary_key=TRUE)
	    SearchQuery= models.CharField(max_length=255)
	 
	

	

	class Donations(models.Model):
	    donationID =models.IntegerField(max_length=20,primary_key=True)
	    donation_date=models.DateField()
	    additional_comments=models.CharField(max_length=100)
	

	class EBDGFOOD(models.Model):
	    EDBGEvent_foodID= models.IntegerField(max_length=20,primary_key=True)
	    ServingsPerGallon=models.IntegerField(max_length=20)
	    EBDGtype=models.CharField(max_length=20)
	    RestaurantName=models.CharField(max_length=100)
	    
	class EBDGRAFFLE(models.Model):
	    eventID=models.ForeignKey(FUNDRAISINGEVENTS, on_delete=models.CASCADE,primary_key=TRUE)
	    donation=models.CharField(max_length=100)
	

	class EMPTYBOWLRAFFLEAUCTION(models.Model):
	    eventID=models.ForeignKey(FUNDRAISINGEVENTS, on_delete=models.CASCADE,primary_key=TRUE)
	    description=models.CharField(max_length=100)
	    item=models.CharField(max_length=100)
	    status=models.CharField(max_length=100)
	    receivedDate=models.DateField()
	 
	class EMPTYBOWLFOOD(models.Model):
	    EmptyBowlEvent_foodID=models.IntegerField(max_length=20,primary_key=True)
	    food_description=models.CharField(max_length=100)
	    quantity=models.IntegerField(max_length=20)
	    totalServings=models.IntegerField(max_length=20)
	    
	class FOOD(models.Model): 
	    foodEntryID=models.IntegerField(max_length=20,primary_key=True)
	    foodtype=models.CharField(max_length=100)
	    avgCost=models.IntegerField(max_length=20)
	    totalPounds=models.IntegerField(max_length=20)
	    totalValue=models.IntegerField(max_length=20)
	 
	class FOODCATEGORY(models.Model):
	    donationID=models.ForeignKey(DONATIONS, on_delete=models.CASCADE,primary_key=TRUE)
	    categoryID=models.IntegerField(max_length=20)
	    
	class FOODENTRY(models.Model):
	    CategoryID=models.ForeignKey(FOODCATEGORY, on_delete=models.CASCADE)
	    foodEntryID=models.IntegerField(max_length=20,primary_key=True)
	    
	class FOODCATEGORYDESC(models.Model):
	    categoryID=models.ForeignKey(FOODCATEGORY, on_delete=models.CASCADE,primary_key=TRUE)
	    description=models.CharField(max_length=100)
	    categoryName=models.CharField(max_length=100)
	 
	class FUNDRAISINGEVENTS(models.Model):
	eventID=models.IntegerField(max_length=20,primary_key=True)
	estimatedValue=models.IntegerField(max_length=20)
	receivedDate=models.DateField()
	location=models.CharField(max_length=100)
	

	class GOLF(models.Model):
	    eventID=models.ForeignKey(FUNDRAISINGEVENTS, on_delete=models.CASCADE,primary_key=TRUE)
	    dtype=models.CharField(max_length=100)
	    
	class ITEMS(models.Model):
	    donationID=models.ForeignKey(DONATIONS, on_delete=models.CASCADE,primary_key=TRUE)
	    description=models.CharField(max_length=100)
	    isack_sent=models.BooleanField(default=False)
	    approxValue=models.IntegerField(max_length=20)
	 
	class MONETARY (models.Model):
	    donationID=models.ForeignKey(DONATIONS, on_delete=models.CASCADE,primary_key=TRUE)
	    amount=models.IntegerField(max_length=20)
	    modeOfPayment=models.CharField(max_length=100)
	 
	class Reports(models.Model):
	    reportID=models.IntegerField(max_length=20,primary_key=True)
	    filename=models.CharField(max_length=100)
	    reportgen_date=models.DateField()
	    
	 class ServiceEvents(models.model)
	service_detailID=models.IntegerField(max_length=20,primary_key=True)
	date_of_service=models.DateField()
	serviceID=models.IntegerField(max_length=20)

#Maria
	class COMP_EDBG(models.Model):
	    EDBGEvent_foodID=models.ForeignKey(EDBGFOOD, on_delete=models.CASCADE,primary_key=TRUE)
	    FoodEntryID=models.ForeignKey(FOOD, on_delete=models.CASCADE,primary_key=TRUE)
	 
	class COMP_EMPTYBOWL(models.Model):
	    EmptyBowlEvent_foodID=models.ForeignKey(EMPTYBOWLFOOD, on_delete=models.CASCADE,primary_key=TRUE)
	    FoodEntryID=models.ForeignKey(FOOD, on_delete=models.CASCADE,primary_key=TRUE)
	   
	class GENERATE(models.Model):
	    userID=models.ForeignKey(USERS, on_delete=models.CASCADE,primary_key=TRUE)
	    reportID=models.ForeignKey(REPORTS, on_delete=models.CASCADE,primary_key=TRUE)
	    
	class INSTRUCT(models.Model):
	    volID=models.ForeignKey(Volunteers, on_delete=models.CASCADE,primary_key=TRUE)
	    service_detailID=models.ForeignKey(SERVICEEVENTS, on_delete=models.CASCADE,primary_key=TRUE)
	    
	class MAINTAIN(models.Model):
	    userID=models.ForeignKey(USERS, on_delete=models.CASCADE,primary_key=TRUE)
	    logID=models.ForeignKey(DonationsLog, on_delete=models.CASCADE,primary_key=TRUE)
	    
	class MAKE_DONATION(models.Model):
	    donorID=models.ForeignKey(DONORS, on_delete=models.CASCADE,primary_key=TRUE)
	    donationID=models.ForeignKey(DONATIONS, on_delete=models.CASCADE,primary_key=TRUE)
	   
	class MANAGE_DONATIONS(models.Model):
	    donationID=models.ForeignKey(DONATIONS, on_delete=models.CASCADE,primary_key=TRUE)
	    userID=models.ForeignKey(USERS, on_delete=models.CASCADE,primary_key=TRUE)
	   
	class ORGANIZES(models.Model):
	    eventID=models.ForeignKey(FUNDRAISINGEVENTS, on_delete=models.CASCADE,primary_key=TRUE)
	    userID=models.ForeignKey(USERS, on_delete=models.CASCADE,primary_key=TRUE)
	    
	class PARTICIPATE_IN(models.Model):
	    eventID=models.ForeignKey(FUNDRAISINGEVENTS, on_delete=models.CASCADE,primary_key=TRUE)
	    donorID=models.ForeignKey(DONORS, on_delete=models.CASCADE,primary_key=TRUE)
	

	class SERVICE_EVENT_DETAILS(models.Model):
	    Service_detailID=models.ForeignKey(SERVICEEVENTS, on_delete=models.CASCADE,primary_key=TRUE)
	    Cust_ID=models.ForeignKey(CUSTOMERS, on_delete=models.CASCADE,primary_key=TRUE)
	    Review = models.CharField(max_length=100)
	    Ratings = models.IntegerField(max_length=20)
	    
	 class SERVICE_OFFER(models.Model):
	    ServiceID=models.ForeignKey(SERVICEEVENTS, on_delete=models.CASCADE,primary_key=TRUE)
	    userID=models.ForeignKey(USERS, on_delete=models.CASCADE,primary_key=TRUE)

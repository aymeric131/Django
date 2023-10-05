from django.http import HttpResponse
from django.shortcuts import render
from listings.models import *

def hello(request):
    bands = Band.objects.all()
    return render(request,'listings/hello.html',
        {'bands': bands})

def about(request):
    return render(request, 'listings/about.html')


def listings(request):
    listings = Listing.objects.all()
    return render(request,'listings/listings.html',context= {'listings' : listings})

def contact(request):
    return render(request, 'listings/contact.html') 
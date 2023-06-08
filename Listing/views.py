from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def listing(request):
    return render(request, 'listing/listing.html')

def contactUs(request):
    return render(request, 'contactUs/contactUs.html')
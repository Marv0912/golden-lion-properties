from django.shortcuts import render, redirect
from .forms import ListingForm

def home(request):
    return render(request, 'home/home.html')

def listing(request):
    return render(request, 'listing/listing.html')

def contactUs(request):
    return render(request, 'contactUs/contactUs.html')

def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else: 
            form = ListingForm()
        return render(request, 'create_listing.html', {'form': form})
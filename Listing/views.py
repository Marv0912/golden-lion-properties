from django.shortcuts import render, redirect
from .forms import ListingForm
from .models import Property

def home(request):
    properties = Property.objects.all()
    return render(request, 'home/home.html', {'properties': properties})

def listing(request, listing_id):
    property = Property.objects.get(id=listing_id)
    return render(request, 'listing/listing_details.html', {'property': property})

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
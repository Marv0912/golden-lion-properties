from django.shortcuts import render, redirect
from .forms import ListingForm
from .models import Property
from django.shortcuts import get_object_or_404

def home(request):
    properties = Property.objects.all()
    return render(request, 'home/home.html', {'properties': properties})

def listing(request, listing_id):
    property = get_object_or_404(Property, id=listing_id)
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
from django.shortcuts import render, redirect
from .forms import ListingForm, ContactForm
from .models import Property
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
# By using the View class, you have the flexibility to define the HTTP methods (GET, POST, PUT, DELETE, etc.) and handle the corresponding logic within your view methods.

def home(request):
    properties = Property.objects.all()
    return render(request, 'home/home.html', {'properties': properties})

def listing(request, listing_id):
    property = get_object_or_404(Property)
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
    
class ContactFormView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact_form.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

             # TODO: Perform any necessary processing or database operations
            # You can save the message to the database or send email notifications here

            # Optionally, you can send an email notification to the admin
            # Uncomment the following lines and customize them based on your needs
            # admin_email = 'admin@example.com'
            # send_email_to_admin(admin_email, name, email, subject, message)

            return render(request, 'contact_success.html')
        else:
            return render(request, 'contact_form.html', {'form': form})
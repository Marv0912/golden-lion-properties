from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from .forms import ListingForm, ContactForm, PropertySearchForm
from .models import Property

# By using the View class, you have the flexibility to define the HTTP methods (GET, POST, PUT, DELETE, etc.) and handle the corresponding logic within your view methods.

def home(request):
    properties = Property.objects.all()
    return render(request, 'home/home.html', {'properties': properties})

def listing(request, listing_id):
    property = get_object_or_404(Property, id=listing_id)
    return render(request, 'listing/listing_details.html', {'property': property})

def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else: 
            form = ListingForm()
        return render(request, 'create_listing.html', {'form': form})
    
class ContactFormView(FormView):
    template_name = 'contactUs/contactUs.html'
    form_class = ContactForm
    success_url = '/'  # Replace with the appropriate URL

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def send_email_to_admin(self, form_data):
        admin_email = 'marvin.fajardo.s@icloud.com'
        subject = f"New Contact Message: {form_data['subject']}"
        message = f"Name: {form_data['name']}\nEmail: {form_data['email']}\n\n{form_data['message']}"
        send_mail(
            subject, 
            message,
            [admin_email],
            )
        # Process the form data here
        # You can save the message to the database or send email notifications

        # Optionally, you can send an email notification to the admin
        # Uncomment the following lines and customize them based on your needs
        # admin_email = 'admin@example.com'
        # send_email_to_admin(admin_email, form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['subject'], form.cleaned_data['message'])

def property_search_view(request):
    form = PropertySearchForm(request.GET or None)
    if request.method == 'POST':
        form = PropertySearchForm(request.POST)
        
    if form.is_valid():
        price_min = form.cleaned_data['price_min']
        price_max = form.cleaned_data['price_max']
        bedrooms = form.cleaned_data['bedrooms']
        bathrooms = form.cleaned_data['bathrooms']

        # Perform the search query using filter conditions
        properties = Property.objects.filter(
            price__range=(price_min, price_max),
            bedrooms=bedrooms,
            bathrooms=bathrooms
        )

        context = {
            'properties': properties
        }
        return render(request, 'search/search_results.html', context)

    context = {
        'form': form
    }
    return render(request, 'search/property_search.html', context)
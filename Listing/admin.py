from django.contrib import admin

# Register your models here.
from .models import Property, ContactMessage
from .forms import ListingForm

class ListingAdmin(admin.ModelAdmin):
    form = ListingForm

admin.site.register(Property, ListingAdmin, ContactMessage)
from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    
    def verify_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("Price cannot be negative. ")
    class Meta:
        model = Listing
        fields = '__all__'
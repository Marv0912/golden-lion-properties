from django import forms
from .models import Property, ContactMessage

class ListingForm(forms.ModelForm):
    
    def verify_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("Price cannot be negative. ")
    class Meta:
        model = Property
        fields = '__all__'


class ContactForm(forms.ModelForm):
   class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

class PropertySearchForm(forms.Form):
    price_min = forms.IntegerField(label='Minimum Price', required=False)
    price_max = forms.IntegerField(label='Maximum Price', required=False)
    bedrooms = forms.IntegerField(label='Bedrooms', required=False)
    bathrooms = forms.DecimalField(label='Bathrooms', required=False)

    def clean(self):
        cleaned_data = super().clean()
        price_min = cleaned_data.get('price_min')
        price_max = cleaned_data.get('price_max')
        
        if price_min and price_max and price_min > price_max:
            raise forms.ValidationError("Minimum price cannot be greater than maximum price.")
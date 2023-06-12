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


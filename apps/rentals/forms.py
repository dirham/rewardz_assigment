from django import forms
from django.utils import timezone
from datetime import timedelta
from .models import Rental

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['user', 'book', 'end_date', 'return_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set initial value for free_end_date based on the default function in the model
        if not self.instance.pk:  # If it's a new instance, set the default
            self.fields['end_date'].initial = timezone.now().date() + timedelta(days=30)
        
        # Customize other field widgets or labels if needed
        self.fields['user'].label = "Select User"
        self.fields['book'].label = "Select Book"
        self.fields['end_date'].widget = forms.SelectDateWidget()  # Use a date picker
        self.fields['return_date'].widget = forms.SelectDateWidget()  # Customize return date with a date picker

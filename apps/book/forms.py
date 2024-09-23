from django import forms
from django.utils import timezone
from datetime import timedelta
from .models import Book

class RentalForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['olid', 'title', 'author', 'page_count']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
         
        self.fields['olid'].label = "Open Library ID"
        self.fields['title'].label = "Book Title"
        self.fields['author'].label = "Author"
        self.fields['page_count'].label = "Page Count"

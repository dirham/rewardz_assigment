from django import forms

class DashboardRentForm(forms.Form):
    book_title = forms.CharField(
        max_length=255,
        required=True,
        error_messages={'required': 'Book title is required.'}
    )
    
    book_author = forms.CharField(
        max_length=255,
        required=True,
        error_messages={'required': 'Book author is required.'}
    )

    book_pages = forms.IntegerField(
        required=True,
        error_messages={'required': 'Page count is required.', 'invalid': 'Enter a valid page count.'}
    )

    olid = forms.CharField(
        max_length=255,
        required=True,
        error_messages={'required': 'OLID is required.'}
    )

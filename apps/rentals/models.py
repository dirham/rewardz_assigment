from datetime import timedelta
from django.db import models
from django.utils import timezone
from apps.book.models import Book
from apps.user.models import Profile
from datetime import date


def default_end_date():
    return timezone.now().date() + timedelta(days=30)

class Rental(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(default=default_end_date, blank=False)  # Expected return date
    return_date = models.DateField(null=True, blank=True)  # Actual return date
    approved = models.BooleanField(default=True)  # Used when a student applies for book rent by them self

    def calculate_fee(self) -> float:
        print('called')
        """
        Calculate the late fee for a book rental based on the number of days rented.
        The first 30 days are free. For each full month after the initial free month, 
        the fee is calculated as the book's page count divided by 100. 
        Extra days are charged as a full month.

        Returns:
            float: The total late fee for the rental. Returns 0 if no fee is incurred.
        """
        # Use the return date if it exists, otherwise use today's date
        current_date = self.return_date if self.return_date else date.today()
        
        # Calculate the total number of rental days
        days_of_rent = (current_date - self.start_date).days
        
        if days_of_rent > 30:
            # Calculate the number of full months beyond the first 30 days
            full_months = (days_of_rent - 30) // 30

            # Check if there are remaining days beyond the full months
            remaining_days = (days_of_rent - 30) % 30

            # Initial fee based on the number of full months
            fee = full_months * (self.book.page_count / 100)

            # If there are remaining days, charge for another full month
            if remaining_days > 0:
                fee += (self.book.page_count / 100)

            return fee
        
        # No fee if the rental period is within the first 30 days
        return 0.0

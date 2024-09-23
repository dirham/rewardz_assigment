import json
from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.core.paginator import Paginator
from django.db.models import Count

from apps.book.services.openlibrary import search
from asgiref.sync import sync_to_async

from apps.user.models import Profile
from .forms import DashboardRentForm
from apps.rentals.models import Rental
from apps.book.models import Book
from apps.user.decorators import librarian_required, student_required

@require_GET
@librarian_required
def index(request):
        if request.GET.get('q'):
            res = search(request.GET.get('q'))
            data = json.loads(res.content)
            # Wrap the render call in sync_to_async
            return render(request, 'dashboard/index.html', {'data': data})

        return render(request, 'dashboard/index.html', {'test': 'some'})

@require_POST
@login_required
def process_rent(request):
        form = DashboardRentForm(request.POST)
        if form.is_valid():
            rent_book, _ = Book.objects.get_or_create(
                    olid=form.cleaned_data['olid'], 
                    defaults={
                        'title': form.cleaned_data['book_title'], 
                        'author': form.cleaned_data['book_author'], 
                        'page_count': form.cleaned_data['book_pages'],
                        }
                )
            
            Rental.objects.create(user=request.user, book=rent_book)
            
            messages.success(request, f'rent success for {rent_book.title}')
            return redirect('dashboard')
        else:
            next = request.POST.get('next', 'dahsboard')
            messages.error(request, form.errors)
            return redirect(next)
    
@login_required
def rented_book(request):
    rent_books = (
        Rental.objects
        .select_related('user', 'book')  # Use select_related to get the related User and Book instances
        .annotate(rental_count=Count('id'))  # Count occurrences
        .order_by('user__username', 'book__title')  # Order results
    )

    paginator = Paginator(rent_books, 10) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'dashboard/rented_books.html', context={'page_obj': page_obj})
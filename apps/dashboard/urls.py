from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='dashboard'),
    path('process_rent/', views.process_rent,name='process_rent'),
    path('rented_books/', views.rented_book, name='rented_books'),
]
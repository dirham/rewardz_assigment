from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.sign_up, name='register'),
    path('', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('get_student/', views.get_student, name='get_student')
]
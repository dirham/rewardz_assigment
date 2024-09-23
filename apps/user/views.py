from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.http import require_GET
from django.contrib.auth.models import Group
from .forms import RegistrationForm, SignInForm
from django.db.models import Q


from .models import Profile 

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Login success')
                return redirect('dashboard')

    form = SignInForm()
    return render(request,'user/login.html', {'form': form})

def sign_up(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'user/register.html', {'form': form})
 
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            # add to student group
            student_group = Group.objects.get(name='Student')
            student_group.user_set.add(user)

            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'user/register.html', {'form': form})

def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')  

@require_GET
def get_student(request):
    name = request.GET.get('name')
    group_name = 'Student' 

    user = Profile.objects.filter(
        Q(username__icontains=name),
        Q(profile__groups__name=group_name) 
    ).values('id').first()
    return JsonResponse(user)

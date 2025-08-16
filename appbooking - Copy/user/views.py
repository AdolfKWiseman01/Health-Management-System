# Placeholder view for book_appointment
def book_appointment(request, doctor_id):
    # You can implement booking logic here later
    return HttpResponse(f"Book appointment for doctor id {doctor_id}")
# Placeholder view for doctor_list
def doctor_list(request):
    return render(request, 'doc_test.html') # change (16.8.2025) When back button click from book appointment
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib import messages

def index(request):
    return render(request, 'index.html')
def doc_test(request):
    return render(request, 'doc_test.html')

def test_p_final(request):
    return render(request, 'test_p_final.html')

def patient_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('patient_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'patient_login.html')

def patient_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully!')
            return redirect('patient_login')
    return render(request, 'patient_signup.html')

def doctor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Check if user is in Doctor group
            if user.groups.filter(name='Doctor').exists():
                login(request, user)
                return redirect('doctor_dashboard')
            else:
                messages.error(request, f'User "{username}" is not in the Doctor group.')
        else:
            # Check if user exists at all
            if User.objects.filter(username=username).exists():
                messages.error(request, f'User "{username}" exists but password is incorrect.')
            else:
                messages.error(request, f'User "{username}" does not exist.')
    return render(request, 'doctor_login.html')

def appointment_form(request):
    # Dummy doctor object for template rendering
    doctor = {
        'id': 1,
        'name': 'Dr. Example',
        'specialization': 'General Medicine',
        'available_days': 'Mon-Fri',
        'start_time': '09:00',
        'end_time': '17:00',
    }
    return render(request, 'appointment_form.html', {'doctor': doctor})

@login_required(login_url='patient_login')
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

@login_required(login_url='doctor_login')
def doctor_dashboard(request):
    # Only allow users in Doctor group
    if not request.user.groups.filter(name='Doctor').exists():
        messages.error(request, 'You are not authorized to access the doctor dashboard.')
        return redirect('doctor_login')
    return render(request, 'doctor_dashboard.html')

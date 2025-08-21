from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from .models import Doctor, Appointment

from .models import Patient, Doctor, Appointment


# ---------- Public Views ----------
def index(request):
    return render(request, 'index.html')

def doc_test(request):
    return render(request, 'doc_test.html')

def test_p_final(request):
    return render(request, 'test_p_final.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        full_message = f"Message from {name} ({email}):\n\n{message}"

        try:
            send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
            messages.success(request, "Your message has been sent successfully ✅")
            return redirect("contact")
        except Exception as e:
            messages.error(request, f"Something went wrong: {e} ❌")

    return render(request, "contact.html")


# ---------- Authentication ----------
def patient_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            Patient.objects.create(
                user=user,
                phone=phone,
                age=age or None,
                gender=gender,
                address=address
            )
            messages.success(request, 'Account created successfully!')
            return redirect('patient_login')

    return render(request, 'patient_signup.html')


def patient_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('patient_dashboard')
        messages.error(request, 'Invalid username or password.')
    return render(request, 'patient_login.html')


def doctor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if user.groups.filter(name='Doctor').exists():
                login(request, user)
                return redirect('doctor_dashboard')
            messages.error(request, f'User "{username}" is not in the Doctor group.')
        else:
            messages.error(request, f'Invalid credentials for "{username}".')
    return render(request, 'doctor_login.html')


# ---------- Dashboards ----------
@login_required(login_url='patient_login')
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')


@login_required(login_url='doctor_login')
def doctor_dashboard(request):
    if not request.user.groups.filter(name='Doctor').exists():
        messages.error(request, 'You are not authorized to access the doctor dashboard.')
        return redirect('doctor_login')
    return render(request, 'doctor_dashboard.html')




def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, "doctor_list.html", {"doctors": doctors})

def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == "POST":
        patient_name = request.POST.get("full_name")
        patient_email = request.POST.get("email")
        patient_phone = request.POST.get("phone")
        appointment_date = request.POST.get("date")
        appointment_time = request.POST.get("time")
        notes = request.POST.get("message")

        # Save appointment using correct field names
        Appointment.objects.create(
            doctor=doctor,
            patient_name=patient_name,
            patient_email=patient_email,
            patient_phone=patient_phone,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            notes=notes
        )

        return redirect("doctor_list")  # go back to doctor list after booking

    return render(request, "book_appointment.html", {
        "doctor": doctor,
        "today": now().date()
    })


def appointment_success(request):
    return render(request, "appointment_success.html")

def patient_profile(request):
    return render(request, "profile.html")





@login_required(login_url='patient_login')
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    # Try to find patient profile if logged in
    patient = Patient.objects.filter(user=request.user).first()

    if request.method == "POST":
        Appointment.objects.create(
            doctor=doctor,
            patient_name=request.user.get_full_name() or request.POST.get("full_name"),
            patient_email=request.user.email or request.POST.get("email"),
            patient_phone=patient.phone if patient else request.POST.get("phone"),
            appointment_date=request.POST.get("date"),
            appointment_time=request.POST.get("time"),
            notes=request.POST.get("message", "")
        )
        return redirect("appointment_success")

    return render(request, "book_appointment.html", {
        "doctor": doctor,
        "today": now().date(),
        "patient_name": request.user.get_full_name() or "",
        "patient_email": request.user.email or "",
        "patient_phone": patient.phone if patient else "",
    })

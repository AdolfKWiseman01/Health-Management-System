from django.contrib import admin
from .models import Doctor, Appointment

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'department', 'start_time', 'end_time', 'available_days')
    search_fields = ('name', 'specialization', 'department')
    list_filter = ('department', 'specialization')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'doctor', 'appointment_date', 'appointment_time', 'created_at')
    list_filter = ('doctor', 'appointment_date')
    search_fields = ('patient_name', 'patient_email', 'patient_phone')
    date_hierarchy = 'appointment_date'

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment, AppointmentAdmin)
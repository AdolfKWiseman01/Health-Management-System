from django.contrib import admin
from django.urls import path
from user import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    # Public pages
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('doc_test.html', views.doc_test, name='doc_test'),
    path('test_p_final.html', views.test_p_final, name='test_p_final'),
    path('contact.html', views.contact, name='contact'),

    # Authentication
    path('patient_signup.html', views.patient_signup, name='patient_signup'),
    path('patient_login.html', views.patient_login, name='patient_login'),
    path('doctor_login.html', views.doctor_login, name='doctor_login'),

    # Dashboards
    path('patient_dashboard.html', views.patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard.html', views.doctor_dashboard, name='doctor_dashboard'),

    # Doctor list
    path('doctor_list.html', views.doctor_list, name='doctor_list'),

    # Appointment booking
    path('<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('appointment_success/', views.appointment_success, name='appointment_success'),

    path("profile.html", views.patient_profile, name="patient_profile"),
    path('patient/profile/', views.patient_profile, name='patient_profile'),
    
    

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

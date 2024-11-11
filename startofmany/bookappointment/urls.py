from django.urls import path
from . import views

app_name = 'bookappointment'
urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('request/', views.request, name='request'),
    path('request_list/', views.request_list, name='request_list'),
]

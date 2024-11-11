from django.contrib.auth.decorators import login_required
from users.decorators import role_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Appointment, MeetingRequest
from .forms import AppointmentForm, MeetingRequestForm


@login_required
@role_required('client')
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Appointment booked successfully!")
    else:
        form = AppointmentForm()
    return render(request, 'bookappointment/book.html', {'form': form})

@login_required
@role_required('manager')
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'bookappointment/appointments.html', {'appointments': appointments})


@login_required
@role_required('videoeditor')
def request(request):
    if request.method == 'POST':
        form = MeetingRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("requets_list")
    else:
        form = MeetingRequestForm()
    return render(request, 'bookappointment/request_meeting.html', {'form': form})

@login_required
@role_required('manager')
def request_list(request):
    meeting_request = MeetingRequest.objects.all()
    return render(request, 'bookappointment/request_list.html', {'meeting_request': meeting_request})

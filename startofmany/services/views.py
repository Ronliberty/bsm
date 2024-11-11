from django.contrib.auth.decorators import login_required
from users.decorators import role_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ServiceForm, ServiceRequestForm
from .models import Service, ServiceRequest
from django.http import HttpResponseForbidden
@login_required
@role_required('manager')
def upload_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('services:services_list')
    else:
        form = ServiceForm()
    return render(request, 'services/upload_service.html', {'form': form})
@login_required
@role_required('manager')
def services_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

@login_required
@role_required('client')
def display_services(request):
    services = Service.objects.all()
    return render(request, 'services/display_services.html', {'services': services})

@login_required
@role_required('client')
def request_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.service = service
            service_request.save()
            return redirect('services:display_requested_services')
    else:
        form = ServiceRequestForm()

    return render(request, 'services/request_service.html', {'service': service, 'form': form})

@login_required
@role_required('client')
def display_requested_services(request):
    if request.user.role != 'client':
        return HttpResponseForbidden("You do not have permission to view this page.")

    requested_services = ServiceRequest.objects.filter(user_id=request.user.id)


    return render(request, 'services/display_requested_services.html', {'requested_services': requested_services})
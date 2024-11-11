from django.contrib.auth.decorators import login_required
from users.decorators import role_required
from django.shortcuts import render, redirect
from .models import Project
from.forms import ProjectForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

@login_required
@role_required('manager')
def create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project:create_list')
    else:
        form = ProjectForm()

    return render(request, 'project/create_project.html', {'form': form})

@login_required
@role_required('manager')
def create_list(request):
    projects = Project.objects.all
    return render(request, 'project/create_list.html', {'projects': projects})

@login_required
@role_required('videoeditor')
def available(request):
    projects = Project.objects.filter(status='available')
    return render(request, 'project/available.html', {'projects': projects})

@login_required
@role_required('videoeditor')
def ongoing(request):
    projects = Project.objects.filter(assigned_to=request.user, status='ongoing')
    return render(request, 'project/ongoing.html', {'projects': projects})

  # Allow only users with the 'manager' role to view this list
@login_required
@role_required('manager')
def ongoing_list(request):
    # Retrieve all projects that are marked as ongoing and have an assigned user
    ongoing_projects = Project.objects.filter(status='ongoing').select_related('assigned_to').order_by('-created_at')
    return render(request, 'project/ongoing_list.html', {'ongoing_projects': ongoing_projects})

@login_required
@role_required('videoeditor')
def complete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, status='ongoing', assigned_to=request.user)

    if request.method == "POST":
        project.status = 'completed'
        project.file = request.FILES.get('file')
        project.save()
        return redirect('project:history')

    return render(request, 'project/complete_project.html', {'project': project})

@login_required
@role_required('videoeditor')
def history(request):
    completed_projects = Project.objects.filter(status='completed', assigned_to=request.user)
    return render(request, 'project/history.html', {'completed_projects': completed_projects})

@login_required
@role_required('manager')
def history_list(request):
    all_completed_projects = Project.objects.filter(status='completed')
    return render(request, 'project/history_list.html', {'completed_projects': all_completed_projects})

@login_required
@role_required('videoeditor')
def take_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, status='available', assigned_to__isnull=True)

    # Check if the project is already taken by someone else
    if project.status == 'ongoing' or project.assigned_to:
        return HttpResponseForbidden("This project is no longer available.")

    # Assign the project to the current user and update status
    project.assigned_to = request.user
    project.status = 'ongoing'
    project.save()

    return redirect('project:ongoing')
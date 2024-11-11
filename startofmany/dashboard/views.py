from django.contrib.auth.decorators import login_required
from users.decorators import role_required
from django.shortcuts import render

# Create your views here.
@login_required
@role_required('manager')
def DashboardView(request):

    return render(request, 'dashboard/dashboard.html')
@login_required
@role_required('videoeditor')
def EditorView(request):

    return render(request, 'dashboard/editor_dashboard.html')

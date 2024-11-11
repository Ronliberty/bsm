# In views.py
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .decorators import role_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from .forms import VideoEditorRegistrationForm, ClientRegistrationForm, ProfileUpdateForm, UserUpdateForm, CustomPasswordChangeForm
from .models import CustomUser, UserProfile




class EmployeeLoginView(LoginView):
    template_name = 'users/employee_login.html'
    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)

        # Redirect based on the user's role
        if user.role == 'manager':
            return redirect(reverse_lazy('dashboard:dashboard'))
        elif user.role == 'videoeditor':
            return redirect(reverse_lazy('dashboard:editor_dashboard'))

        else:
            return redirect('users:client_login')  # For clients


class ClientLoginView(LoginView):
    template_name = 'users/login.html'  # Separate login template for clients
    success_url = reverse_lazy('users:client_dashboard')  # URL after successful client login

    def form_valid(self, form):
        user = form.get_user()
        if user.role == 'client':
            login(self.request, user)
            return redirect(self.success_url)
        else:
            return redirect('users:client_login')

class VideoEditorSignUpView(CreateView):
    model = CustomUser
    form_class = VideoEditorRegistrationForm
    template_name = 'users/editor_signup.html'  # Template for video editor sign-up
    success_url = reverse_lazy('dashboard:editor_dashboard')  # Redirect to their dashboard after sign-up

    def form_valid(self, form):
        user = form.save(commit=False)
        user.role = 'videoeditor'
        user.save()
        login(self.request, user)
        return super().form_valid(form)


class ClientSignUpView(CreateView):
    model = CustomUser
    form_class = ClientRegistrationForm
    template_name = 'users/signin.html'
    success_url = reverse_lazy('users:client_login')  # Redirect to client dashboard after sign-up

    def form_valid(self, form):
        user = form.save(commit=False)
        user.role = 'client'
        user.save()
        login(self.request, user)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_signup'] = True  # Set `is_signup` to True to display signup form
        return context




@login_required
@role_required('client')
def ClientDashboardView(request):

    return render(request, 'users/client_dashboard.html')

@login_required
@role_required('manager')
def manager_profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    form = ProfileUpdateForm(instance=user_profile)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('users:manager_profile')
        else:
            form = ProfileUpdateForm(instance=user_profile)


    return render(request, 'users/manager_profile.html', {'form': form})

@login_required
@role_required('videoeditor')
def video_editor_profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)


    form = ProfileUpdateForm(instance=user_profile)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('users:video_editor_profile')


    return render(request, 'users/editor_profile.html', {'form': form})

@login_required
@role_required('client')
def client_profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)


    form = ProfileUpdateForm(instance=user_profile)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('users:client_profile')


    return render(request, 'users/client_profile.html', {'form': form})

@login_required
@role_required('manager')
def manager_user_update_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('users:manager_user_update')
    else:
        form = UserUpdateForm(instance=request.user)  # This line handles GET requests

    return render(request, 'users/manager_update.html', {'form': form})

@login_required
@role_required('client')
def client_user_update_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('users:client_user_update')
    else:
        form = UserUpdateForm(instance=request.user)  # This line handles GET requests

    return render(request, 'users/client_update.html', {'form': form})

@login_required
@role_required('videoeditor')
def videoeditor_user_update_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('users:videoeditor_user_update')
    else:
        form = UserUpdateForm(instance=request.user)  # This line handles GET requests

    return render(request, 'users/videoeditor_update.html', {'form': form})


@login_required
@role_required('manager')
def manager_password_change_view(request):
    if request.method == 'POST':
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            password_form.save()
            messages.success(request, 'Your password has been changed successfully!')
            return redirect('users:employee_login')  # Redirect to the login page or another page
    else:
        password_form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'users/manager_password.html', {'password_form': password_form})

@login_required
@role_required('client')
def client_password_change_view(request):
    if request.method == 'POST':
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            password_form.save()
            messages.success(request, 'Your password has been changed successfully!')
            return redirect('users:client_login')  # Redirect to the login page or another page
    else:
        password_form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'users/client_password.html', {'password_form': password_form})

@login_required# View for Video Editors to change their password
@role_required('videoeditor')
def videoeditor_password_change_view(request):
    if request.method == 'POST':
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            password_form.save()
            messages.success(request, 'Your password has been changed successfully!')
            return redirect('users:employee_login')  # Redirect to the login page or another page
    else:
        password_form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'users/videoeditor_password.html', {'password_form': password_form})

from django.urls import path
from .views import (
    EmployeeLoginView, ClientLoginView, ClientDashboardView,
    VideoEditorSignUpView, ClientSignUpView,
    manager_profile_view, video_editor_profile_view, client_profile_view, manager_user_update_view, client_user_update_view, videoeditor_user_update_view,
manager_password_change_view, client_password_change_view, videoeditor_password_change_view
)

app_name = 'users'

urlpatterns = [
    path('login/employee/', EmployeeLoginView.as_view(), name='employee_login'),
    path('login/client/', ClientLoginView.as_view(), name='client_login'),
    path('signup/videoeditor/', VideoEditorSignUpView.as_view(), name='videoeditor_signup'),
    path('signup/client/', ClientSignUpView.as_view(), name='client_signup'),
    path('dashboard/', ClientDashboardView, name='client_dashboard'),
    path('profile/manager/', manager_profile_view, name='manager_profile'),
    path('profile/videoeditor/', video_editor_profile_view, name='video_editor_profile'),
    path('profile/client/', client_profile_view, name='client_profile'),
    path('manager/profile/update/', manager_user_update_view, name='manager_user_update'),
    path('client/profile/update/', client_user_update_view, name='client_user_update'),
    path('videoeditor/profile/update/', videoeditor_user_update_view, name='videoeditor_user_update'),
    path('manager/password/change/', manager_password_change_view, name='manager_password_change'),
    path('client/password/change/', client_password_change_view, name='client_password_change'),
    path('videoeditor/password/change/', videoeditor_password_change_view, name='videoeditor_password_change'),
]

from django.urls import path
from . import views

app_name = 'project'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('create_list/', views.create_list, name='create_list'),
    path('available/', views.available, name='available'),
    path('take/<int:project_id>/', views.take_project, name='take_project'),
    path('ongoing/', views.ongoing, name='ongoing'),
    path('ongoing_list/', views.ongoing_list, name='ongoing_list'),
    path('complete/<int:project_id>/', views.complete_project, name='complete_project'),  # URL for completing a project
    path('history/', views.history, name='history'),  # URL for user's completed projects
    path('history_list/', views.history_list, name='history_list'),  # URL for all completed projects
    path('take/<int:project_id>/', views.take_project, name='take_project'),

]

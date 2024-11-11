from django.urls import path
from .views import DashboardView, EditorView


app_name = 'dashboard'
urlpatterns = [

    path('dashboard/', DashboardView, name='dashboard'),
path('editor/', EditorView, name='editor_dashboard'),
]

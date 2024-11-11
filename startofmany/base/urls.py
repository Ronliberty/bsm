from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.index, name='index'),


    # URLs for independent section handling
    path('section/<str:section_name>/', views.section_view, name='section'),
    path('section/<str:section_name>/delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('landing', views.landing, name='landing'),
]


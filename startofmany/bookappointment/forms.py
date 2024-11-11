# bookappointment/forms.py
from django import forms
from .models import Appointment, MeetingRequest

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'description']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'style': 'width: 80%; padding: 5px; margin-bottom: 10px; border-radius: 5px; border: 1px solid black;'
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'style': 'width: 80%; padding: 5px; margin-bottom: 10px; border-radius: 5px; border: 1px solid black;'
            }),
            'description': forms.TextInput(attrs={
                'style': 'width: 80%; height: 100px; margin-bottom: 20px; padding: 5px; border-radius: 5px; border: 1px solid black;'
            }),
        }

class MeetingRequestForm(forms.ModelForm):
    class Meta:
        model = MeetingRequest
        fields = ['name', 'email', 'date', 'time', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'style': 'width: 70%; padding: 10px; border: 1px solid black; border-radius: 5px; margin-bottom: 20px; margin-left: 10px; background-color: transparent'}),
            'email': forms.EmailInput(attrs={'style': 'width: 70%; padding: 10px; border-radius: 5px; border: 1px solid black; margin-bottom: 20px; margin-left: 10px; background-color: transparent;'}),
            'date': forms.DateInput(attrs={'type': 'date', 'style': 'width: 70%; border-radius: 5px; padding: 10px; margin-bottom: 20px; margin-left: 10px; background-color: transparent'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'style': 'width: 70%; border-radius: 5px; padding: 10px; margin-bottom: 20px; margin-left: 10px; background-color: transparent'}),
            'message': forms.Textarea(
                attrs={'style': 'width: 80%; height: 80px; padding: 10px; border-radius: 5px; border: 1px solid black; margin-bottom: 20px; background-color: transparent'})
        }
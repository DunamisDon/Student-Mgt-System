from django import forms
from .models import Student
from django.core.exceptions import ValidationError
from django.db import IntegrityError

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'address', 'form', 'paidFees']
        labels = {
            'student_number': 'Student Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'address': 'Address',
            'form': 'Form',
            'paidFees': 'paidFees'
        }
        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'form': forms.NumberInput(attrs={'class': 'form-control'}),
            'paidFees': forms.CheckboxInput(),
        }
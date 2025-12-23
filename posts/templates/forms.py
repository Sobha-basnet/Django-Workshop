from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['studentName', 'studentAge', 'studentEmail','address']
        # This adds Bootstrap classes to the Django-generated fields
        widgets = {
            'studentName': forms.TextInput(attrs={'class': 'form-control'}),
            'studentAge': forms.NumberInput(attrs={'class': 'form-control'}),
            'studentEmail': forms.EmailInput(attrs={'class': 'form-control'}),
        }
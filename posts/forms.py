from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # These are the fields from your Model
        fields = ['studentName', 'studentEmail', 'age', 'address']
        
        widgets = {
            'studentName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'studentEmail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            # This line specifically makes the address box small/single-line
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Residential Address'}),
        }
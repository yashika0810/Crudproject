from django import forms
from django.db import models
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

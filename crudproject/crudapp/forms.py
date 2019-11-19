from django import forms
from django.db import models
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
<<<<<<< HEAD
        model = Emp
        fields = "__all__"
=======
        model = Student
        fields = "__all__"
>>>>>>> 4b7e119b3696c48ec31e764ba51d428b7561248a

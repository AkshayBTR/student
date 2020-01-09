from django import forms
from myapp.models import *
class Std_Form(forms.ModelForm):
    class Meta:
        model=Student_Details
        fields='__all__'


from django import forms
from .models import User1

class FormModel(forms.ModelForm):


    class Meta():
        model = User1
        fields = '__all__'

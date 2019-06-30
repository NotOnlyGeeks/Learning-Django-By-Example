from django import forms
from django.core import validators

def check_z(value):
    if value[0]!='Z':
        raise forms.ValidationError('Should start with Z')

class FormName(forms.Form):
    FirstName=forms.CharField(widget=forms.TextInput,validators=[validators.MaxLengthValidator(100)])
    LastName=forms.CharField(widget=forms.TextInput,validators=[check_z])
    Email=forms.EmailField(widget=forms.TextInput,validators=[validators.MaxLengthValidator(100)])
    Botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean_Botcatcher(self):
        Botcatcher = self.cleaned_data['Botcatcher']
        if len(Botcatcher)>0:
            raise forms.ValidationError("Bot found!!")
        else:
            return Botcatcher




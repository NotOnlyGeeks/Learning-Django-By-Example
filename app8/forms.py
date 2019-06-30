from django import forms

class FormName(forms.Form):
    FirstName=forms.CharField(widget=forms.TextInput)
    LastName=forms.CharField(widget=forms.TextInput)
    Email=forms.EmailField(widget=forms.TextInput)
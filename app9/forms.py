from django import forms

class FormName(forms.Form):
    FirstName=forms.CharField(widget=forms.TextInput)
    LastName=forms.CharField(widget=forms.TextInput)
    Email=forms.EmailField(widget=forms.EmailInput)
    VerifyEmail=forms.EmailField(widget=forms.EmailInput)

    def clean(self):
        all_cleaned_data=super().clean()
        Email = all_cleaned_data['Email']
        VerifyEmail = all_cleaned_data['VerifyEmail']

        if Email!=VerifyEmail:
            raise forms.ValidationError("Email and verify email does not match!")



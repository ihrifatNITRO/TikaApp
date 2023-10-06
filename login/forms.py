# login/forms.py
from django import forms

class LoginForm(forms.Form):
    nid = forms.CharField(label='NID', max_length=20, required=True, widget=forms.TextInput(attrs={'type': 'number'}))
    pass1 = forms.CharField(label='Password', required=True, widget=forms.PasswordInput)


# from django import forms

# class login_form(forms.Form):
#     email = forms.EmailField(label='Email', required=True)
#     password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
# register/forms.py
from django import forms

class RegistrationForm(forms.Form):
    nid = forms.CharField(label='NID', max_length=20, required=True, widget=forms.TextInput(attrs={'type': 'number'}))
    email = forms.EmailField(label='Email', required=True)
    pass1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    pass2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=True)

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ('name', 'nid', 'email', 'password')
#         widgets = {
#             'password': forms.PasswordInput(),
#         }

#     def clean_nid(self):
#         nid = self.cleaned_data['nid']
        
#         # Check if nid contains only digits
#         if not nid.isdigit():
#             raise forms.ValidationError("NID must contain only digits.")

#         return nid



# from django import forms
# from django.forms import ModelForm
# from .models import Get_Details

# #Create Forms here
# class register_form(forms.ModelForm):
#     # name = forms.CharField(label='Name', max_length=100, required=True)
#     nid = forms.CharField(label='NID', max_length=20, required=True, widget=forms.TextInput(attrs={'type': 'number'}))
#     # email = forms.EmailField(label='Email', required=True)
#     # password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
#     class Meta:
#         model = Get_Details
#         fields = "__all__"
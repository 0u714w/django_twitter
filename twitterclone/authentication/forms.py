from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=75)
    password = forms.CharField(widget=forms.PasswordInput())
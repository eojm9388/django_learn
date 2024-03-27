from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=12, label='')
    password = forms.CharField(widget=forms.PasswordInput, label='')


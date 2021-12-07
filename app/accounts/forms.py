from django import forms
from django.forms import fields
from django.forms.widgets import PasswordInput
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput(
        {
            'placeholder': 'Sua senha'
        }
    ))
    confirm_password = forms.CharField(widget=PasswordInput(
        {
            'placeholder': 'Repita sua senha'
        }
    ))


    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'password']


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        # Registration form parameters placeholder config
        self.fields['first_name'].widget.attrs['placeholder'] = 'Digite seu nome'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Digite seu sobrenome'
        self.fields['email'].widget.attrs['placeholder'] = 'Digite seu email'

        # Adding css class
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem")
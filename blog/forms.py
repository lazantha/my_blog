from django import forms
from .models import UserTable

class UserLogForm(forms.ModelForm):
    class Meta:
        model = UserTable
        fields = ['name','email']

    # dp = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control ','placeholder':'Profile pic'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ','placeholder':'Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control ','placeholder':'Email'}))


class UserRegForm(forms.ModelForm):
    class Meta:
        model=UserTable
        fields='__all__'
    dp = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control ','placeholder':'Profile pic'}),required=False)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ','placeholder':'Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control ','placeholder':'Email'}))

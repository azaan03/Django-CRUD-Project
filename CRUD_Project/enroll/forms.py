from django import forms
from .models import User  

class UserForm(forms.ModelForm):
    class Meta:
        model = User  
        fields = ['name', 'email', 'password']  
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
        }
        labels = {
            'name' : 'Enter Name',
            'email' : 'Enter Email',
            'password' : 'Enter Password',
        }
                  
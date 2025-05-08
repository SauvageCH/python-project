from django import forms
from .models import Contact, CustomUser
#ce fichier contient les classes nécessaires afin de commencer notre login et de gérer 
#l'insertion des données de contact
class LoginForm(forms.Form):
    phone_number = forms.CharField(label="Téléphone")
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'category']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

from django.forms import ModelForm
from .models import Registration

class UserForm(ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'password']
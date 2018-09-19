from django import forms
from user_app.models import User
from django.core import validators

class NewUserForm(forms.ModelForm):
    """docstring for NewUser."""
    class Meta():
        """dotring for Meta."""
        model = User
        fields = '__all__'

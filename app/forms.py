from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.core.validators import FileExtensionValidator

from app.models import User


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['username']
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UploadFile(forms.Form):
    file = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['py'])])

    def __init__(self, *args, **kwargs):
        super(UploadFile, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

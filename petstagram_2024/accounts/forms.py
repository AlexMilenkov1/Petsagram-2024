from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from petstagram_2024.accounts.models import Profile

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email', )


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'date_of_birth': 'Birthdate',
            'profile_picture': 'Picture',
        }


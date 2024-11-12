from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from petstagram_2024.accounts.forms import AppUserCreationForm, ProfileEditForm
from petstagram_2024.accounts.models import Profile

# Create your views here.

UserModel = get_user_model()


class Register(CreateView):
    model = UserModel
    template_name = 'accounts/register-page.html'
    form_class = AppUserCreationForm
    success_url = reverse_lazy('login')


class AppUserLoginView(LoginView):
    template_name = 'accounts/login-page.html'


class AppUserLogoutView(LogoutView):
    pass


def show_profile_details(request, pk):
    return render(request, 'accounts/profile-details-page.html')


class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'accounts/profile-edit-page.html'
    form_class = ProfileEditForm

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.object.pk
            }
        )


def delete_profile(request):
    return render(request, 'accounts/profile-delete-page.html')

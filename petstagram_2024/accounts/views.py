from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

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


class ProfileDetailView(DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['all_likes_count'] = sum(p.likes.count() for p in self.object.photos.all())

        return context


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'accounts/profile-edit-page.html'
    form_class = ProfileEditForm

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.object.pk
            }
        )


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('home-page')

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user
    
    def form_valid(self, form):
        self.object.user.delete()
        
        return super().form_valid(form)
        
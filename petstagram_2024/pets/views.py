from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from petstagram_2024.accounts.models import Profile, UserModel
from petstagram_2024.pets.forms import PetBaseForm, PetEditForm, PetDeleteForm
from petstagram_2024.pets.models import Pet



class AddPage(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = PetBaseForm
    template_name = 'pets/pet-add-page.html'

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.request.user.pk,
            }
        )

class PetDetails(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    pk_url_kwarg = 'pk'
    slug_url_kwarg = 'pet_slug'

    def get_object(self, queryset=None):
        # lookup by both owner and slug
        return get_object_or_404(
            Pet,
            user__pk = self.kwargs['pk'],
            slug = self.kwargs['pet_slug'],
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = self.object
        # pull in only the photos where *this* pet is tagged
        context['all_photos'] = pet.photos_tagged_in.all()
        return context

class EditPet(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pet
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'  # Correct the variable name
    form_class = PetEditForm

    def test_func(self):
        pet = get_object_or_404(Pet, slug=self.kwargs['pet_slug'])
        return self.request.user == pet.user

    def get_success_url(self):
        return reverse_lazy(
            'details-pet',
            kwargs={
                'pk': self.kwargs['pk'],
                'pet_slug': self.kwargs['pet_slug']
            }
        )


class DeletePet(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pet
    form_class = PetDeleteForm
    template_name = 'pets/pet-delete-page.html'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})
    slug_url_kwarg = 'pet_slug'

    def test_func(self):
        pet = get_object_or_404(Pet, slug=self.kwargs['slug'])
        return self.request.user == pet.user

    def get_initial(self):
        return self.object.__dict__

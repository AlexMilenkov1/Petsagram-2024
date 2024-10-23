from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from petstagram_2024.common.forms import CommentForm
from petstagram_2024.pets.forms import PetBaseForm, PetEditForm, PetDeleteForm
from petstagram_2024.pets.models import Pet
from petstagram_2024.photos.models import Photo


class AddPage(CreateView):
    model = Pet
    form_class = PetBaseForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})


class PetDetails(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['all_photos'] = self.object.photos_tagged_in.all()
        return context


class EditPet(UpdateView):
    model = Pet
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'
    form_class = PetEditForm

    def get_success_url(self):
        return reverse_lazy(
            'details-pet',
            kwargs={
                'username': self.kwargs['username'],
                'pet_slug': self.kwargs['pet_slug']
            }
        )


class DeletePet(DeleteView):
    model = Pet
    form_class = PetDeleteForm
    template_name = 'pets/pet-delete-page.html'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})
    slug_url_kwarg = 'pet_slug'

    def get_initial(self):
        return self.object.__dict__

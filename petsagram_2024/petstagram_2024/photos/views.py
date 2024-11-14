from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from petstagram_2024.common.forms import CommentForm
from petstagram_2024.photos.forms import BasePhotoForm, EditPhotoForm
from petstagram_2024.photos.models import Photo


class AddPhoto(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = BasePhotoForm
    template_name = 'photos/photo-add-page.html'

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.request.user.pk
            }
        )


class PhotoDetailsView(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['likes'] = self.object.likes.all()
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm()
        self.object.has_liked = self.object.likes.filter(user=self.request.user).exists()

        return context


class PhotoEditPage(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    form_class = EditPhotoForm
    template_name = 'photos/photo-edit-page.html'

    def test_func(self):
        photo = get_object_or_404(Photo, pk=self.kwargs['pk'])
        return self.request.user == photo.user

    def get_success_url(self):
        return reverse_lazy('details-photo', kwargs={'pk': self.object.pk})


@login_required
def delete_photo(request, pk):
    photo_object = Photo.objects.get(pk=pk)

    if photo_object.user.pk == request.user.pk:
        photo_object.delete()

    return redirect('home-page')

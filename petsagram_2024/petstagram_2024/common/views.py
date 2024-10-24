from django.shortcuts import render, redirect, resolve_url
from django.views.generic import ListView

from petstagram_2024.common.forms import CommentForm, SearchForm
from petstagram_2024.common.models import Like
from petstagram_2024.photos.models import Photo

from pyperclip import copy


class HomePage(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'all_photos'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['search_form'] = SearchForm(self.request.GET)

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_value = self.request.GET.get('pet_name')

        if filter_value:
            queryset = self.model.objects.filter(tagged_pets__name__icontains=filter_value)

        return queryset




def like_functionality(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def share_functionality(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('details-photo', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def comment_functionality(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)

    form = CommentForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

            return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')

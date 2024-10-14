from django.shortcuts import render, redirect, resolve_url

from petstagram_2024.common.forms import CommentForm, SearchForm
from petstagram_2024.common.models import Like
from petstagram_2024.photos.models import Photo

from pyperclip import copy


# Create your views here.
def home_page(request):
    all_photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm(request.GET or None)

    if search_form.is_valid():
        all_photos = all_photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form
    }

    return render(request, 'common/home-page.html', context=context)


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

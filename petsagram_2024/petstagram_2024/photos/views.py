from django.shortcuts import render, redirect

from petstagram_2024.common.forms import CommentForm
from petstagram_2024.photos.forms import BasePhotoForm, EditPhotoForm
from petstagram_2024.photos.models import Photo


# Create your views here.
def add_photo(request):
    form = BasePhotoForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('home-page')

    context = {
        'form': form
    }

    return render(request, 'photos/photo-add-page.html', context)


def details_photo(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    likes = photo.likes.all()
    comments = photo.comments.all()
    comment_form = CommentForm()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comment_form': comment_form
    }

    return render(request, 'photos/photo-details-page.html', context=context)


def edit_photo(request, pk):
    photo_object = Photo.objects.get(pk=pk)
    form = EditPhotoForm(request.POST or None, instance=photo_object)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('details-photo', pk)

    context = {
        'form': form
    }

    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk):
    photo_object = Photo.objects.get(pk=pk)

    photo_object.delete()

    return redirect('home-page')

def test(request):
    pass
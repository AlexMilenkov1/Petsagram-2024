from django.shortcuts import render, redirect

from petstagram_2024.photos.forms import BasePhotoForm
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

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments
    }

    return render(request, 'photos/photo-details-page.html', context=context)


def edit_photo(request, photo_id):
    return render(request, 'photos/photo-edit-page.html')

def delete_photo(request, pk):
    pass
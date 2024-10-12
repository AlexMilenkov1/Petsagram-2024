from django.shortcuts import render

from petstagram_2024.photos.models import Photo


# Create your views here.
def add_photo(request):
    return render(request, 'photos/photo-add-page.html')


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


def edit_photo(request):
    return render(request, 'photos/photo-edit-page.html')

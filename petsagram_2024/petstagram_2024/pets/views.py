from django.shortcuts import render

from petstagram_2024.pets.models import Pet
from petstagram_2024.photos.models import Photo


# Create your views here.
def add_page(request):
    return render(request, 'pets/pet-add-page.html')


def details_page(request, username, pet_slug):
    pet = Pet.objects.get(pet_slug=pet_slug)
    all_photos = pet.photos_tagged_in.all()

    context = {
        'pet': pet,
        'all_photos': all_photos
    }

    return render(request, 'pets/pet-details-page.html')


def edit_page(request):
    return render(request, 'pets/pet-edit-page.html')


def delete_page(request):
    return render(request, 'pets/pet-delete-page.html')

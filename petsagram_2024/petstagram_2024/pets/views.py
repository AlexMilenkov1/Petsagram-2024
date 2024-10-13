from django.shortcuts import render, redirect

from petstagram_2024.pets.forms import PetBaseForm, PetEditForm, PetDeleteForm
from petstagram_2024.pets.models import Pet
from petstagram_2024.photos.models import Photo


# Create your views here.
def add_page(request):
    form = PetBaseForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('profile-details', pk=1)

    context = {
        'form': form
    }

    return render(request, 'pets/pet-add-page.html', context=context)


def details_page(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photos_tagged_in.all()

    context = {
        'pet': pet,
        'all_photos': all_photos
    }

    return render(request, 'pets/pet-details-page.html', context)


def edit_page(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    form = PetEditForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('details-pet', username, pet_slug)

    context = {
        'form': form
    }

    return render(request, 'pets/pet-edit-page.html', context)


def delete_page(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    form = PetDeleteForm(instance=pet)

    if request.method == 'POST':
            pet.delete()
            return redirect('profile-details', pk=1)

    context = {
        'form': form
    }

    return render(request, 'pets/pet-delete-page.html', context)

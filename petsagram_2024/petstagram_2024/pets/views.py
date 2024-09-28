from django.shortcuts import render


# Create your views here.
def add_page(request):
    return render(request, 'pets/pet-add-page.html')


def details_page(request):
    return render(request, 'pets/pet-details-page.html')


def edit_page(request):
    return render(request, 'pets/pet-edit-page.html')


def delete_page(request):
    return render(request, 'pets/pet-delete-page.html')

from django.urls import path, include
from petstagram_2024.pets import views

urlpatterns = [
    path('add/', views.AddPage.as_view(), name='add-pet'),
    path('<int:pk>/pet/<slug:pet_slug>/', include([
        path('', views.PetDetails.as_view(), name='details-pet'),
        path('edit/', views.EditPet.as_view(), name='edit-pet'),
        path('delete/', views.DeletePet.as_view(), name='delete-pet'),
    ])),
]

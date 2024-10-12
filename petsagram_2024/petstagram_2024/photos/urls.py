from django.urls import path

from petstagram_2024.photos import views


urlpatterns = [
    path('add/', views.add_photo, name='add-photo'),
    path('<int:photo_id>/', views.details_photo, name='details-photo'),
    path('<int:pk>/edit/', views.edit_photo, name='edit-photo')
]

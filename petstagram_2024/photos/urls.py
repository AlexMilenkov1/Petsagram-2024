from django.urls import path
from petstagram_2024.photos import views

urlpatterns = [
    path('add/', views.AddPhoto.as_view(), name='add-photo'),
    path('<int:pk>/', views.PhotoDetailsView.as_view(), name='details-photo'),
    path('<int:pk>/edit/', views.PhotoEditPage.as_view(), name='edit-photo'),
    path('<int:pk>/delete/', views.delete_photo, name='delete-photo'),
]

from django.urls import path, include

from petstagram_2024.pets import views

urlpatterns = [
    path('add/', views.add_page, name='add-pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.details_page, name='details-pet'),
        path('edit/', views.edit_page, name='edit-pet'),
        path('delete/', views.delete_page, name='delete-pet')
    ]))
]

from django.urls import path, include

from petstagram_2024.pets import views

urlpatterns = [
    path('add/', views.add_page, name='page-add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.details_page, name='page-details'),
        path('edit/', views.edit_page, name='page-edit'),
        path('delete/', views.delete_page, name='page-delete')
    ]))
]

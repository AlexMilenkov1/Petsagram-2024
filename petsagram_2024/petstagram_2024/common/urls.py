from petstagram_2024.common import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name='home-page')
]

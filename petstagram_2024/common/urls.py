from petstagram_2024.common import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home-page'),
    path('like/<int:photo_id>', views.like_functionality, name='like'),
    path('comment/<int:photo_id>', views.comment_functionality, name='comment')
]

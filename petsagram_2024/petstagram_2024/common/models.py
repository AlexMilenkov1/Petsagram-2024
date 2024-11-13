from django.contrib.auth import get_user_model
from django.db import models

from petstagram_2024.photos.models import Photo

UserModel = get_user_model()


# Create your models here.
class Comment(models.Model):
    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    class Meta:
        ordering = ['-date_time_of_publication']


class Like(models.Model):
    to_photo = models.ForeignKey(Photo, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='likes',
    )
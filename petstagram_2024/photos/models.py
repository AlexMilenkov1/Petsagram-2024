from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram_2024.pets.models import Pet
from petstagram_2024.photos.validators import FileSizeValidator

UserModel = get_user_model()


# Create your models here.
class Photo(models.Model):
    photo = models.ImageField(
        upload_to='images',
        null=False,
        blank=False,
        validators=[
            FileSizeValidator(5)
        ]
    )

    description = models.TextField(
        max_length=300,
        validators=[
            MinLengthValidator(10)
        ],
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=30,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
        related_name='photos_tagged_in'
    )

    date_of_publication = models.DateField(auto_now=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='photos',
    )


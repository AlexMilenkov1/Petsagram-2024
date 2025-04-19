from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

UserModel = get_user_model()

class Pet(models.Model):
    name = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )

    personal_photo = models.ImageField(
        upload_to='pet_photos/',
        blank=False,
        null=False
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='pets',
    )

    def save(self, *args, **kwargs):
        # Save once to generate `id`
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

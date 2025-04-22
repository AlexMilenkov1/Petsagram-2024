from cloudinary.models import CloudinaryField
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

    personal_photo = CloudinaryField(
        'image',  # This will store the image on Cloudinary
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
        if not self.pk:
            # Save once to get a primary key
            super().save(*args, **kwargs)
            # Then generate a slug with a proper ID
            self.slug = slugify(f'{self.name}-{self.id}')
            # Save again to update the slug
            return super().save(update_fields=['slug'])

        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

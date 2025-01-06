from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from petstagram_2024.photos.models import Photo

UserModel = get_user_model()


class DeletePhotoTestView(TestCase):
    def setUp(self):
        self.user_a = UserModel.objects.create_user(
            email='test1@test.gmail',
            password='12admin34'
        )

        self.user_b = UserModel.objects.create_user(
            email='test2@test.gmail',
            password='12admin34'
        )

        self.photo = Photo.objects.create(
            photo='cute_dog.png',
            description='Adorable pet, I love him so much!',
            location='Tokyo',
            user=self.user_a
        )

    def test_get_photo___delete_it__by_owner_of_the_photo(self):
        self.client.login(
            email='test1@test.gmail',
            password='12admin34'
        )

        self.assertTrue(Photo.objects.filter(pk=self.photo.pk).exists())

        response = self.client.post(
            reverse('delete-photo', kwargs={'pk': self.photo.pk})
        )

        self.assertFalse(Photo.objects.filter(pk=self.photo.pk).exists())
        self.assertRedirects(response, reverse('home-page'))

    def test_get_photo__delete_it__by_random_user__not_successful(self):
        self.client.login(
            email='test2@test.gmail',
            password='12admin34'
        )

        response = self.client.post(
            reverse('delete-photo', kwargs={'pk': self.photo.pk})
        )

        self.assertTrue(Photo.objects.filter(pk=self.photo.pk).exists())
        self.assertRedirects(response, reverse('home-page'))

    def test_anonymous_user__deleting_photo__not_successful(self):
        response = self.client.post(
            reverse('delete-photo', kwargs={'pk': self.photo.pk})
        )

        self.assertTrue(Photo.objects.filter(pk=self.photo.pk).exists())
        self.assertRedirects(response, f'{reverse('login')}?next=/photos/{self.photo.pk}/delete/')
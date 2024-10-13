from django import forms

from petstagram_2024.photos.models import Photo


class BasePhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
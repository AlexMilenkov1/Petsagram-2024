from django import forms

from petstagram_2024.photos.models import Photo


class BasePhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'


class EditPhotoForm(BasePhotoForm):
    class Meta:
        model = Photo
        exclude = ['photo']


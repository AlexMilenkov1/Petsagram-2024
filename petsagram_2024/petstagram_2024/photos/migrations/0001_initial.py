# Generated by Django 5.1.1 on 2024-09-29 08:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True, max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('location', models.CharField(max_length=30)),
                ('date_of_publication', models.DateField(auto_now=True)),
                ('tagged_pets', models.ManyToManyField(blank=True, null=True, related_name='photos_tagged_in', to='pets.pet')),
            ],
        ),
    ]
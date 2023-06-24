from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def validate_profile_name(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


class ProfileModel(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[
            validators.MinLengthValidator(2),
            validate_profile_name,
        ],
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=35,
        validators=[
            validators.MinLengthValidator(1),
            validate_profile_name,
        ],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        max_length=40,
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=20,
        validators=[
            validators.MinLengthValidator(8),
        ],
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    age = models.IntegerField(
        default=18,
        null=True,
        blank=True,
    )


def validate_fruit_name(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError("Fruit name should contain only letters!")


class FruitModel(models.Model):
    class Meta:
        ordering = ('pk',)

    name = models.CharField(
        max_length=30,
        validators=[
            validators.MinLengthValidator(2),
            validate_fruit_name,
        ],
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

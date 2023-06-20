from enum import Enum

from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def validate_profile_name(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


class ProfileModel(models.Model):
    MAX_LENGTH_USERNAME = 10
    MIN_LENGTH_USERNAME = 2
    MAX_LENGTH_NAME = 20

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=[
            validators.MinLengthValidator(MIN_LENGTH_USERNAME),
        ],
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=[
            validate_profile_name,
        ],
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=[
            validate_profile_name,
        ],
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


def validate_plant_name(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError("Plant name should contain only letters!")


class PlantTypes(Enum):
    OUTDOOR = "Outdoor Plants"
    INDOOR = "Indoor Plants"

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class PlantModel(models.Model):
    class Meta:
        ordering = ('pk',)

    MAX_LENGTH_PLANT_TYPE = 14
    MAX_LENGTH_NAME = 20
    MIN_LENGTH_NAME = 2

    plant_type = models.CharField(
        max_length=MAX_LENGTH_PLANT_TYPE,
        choices=PlantTypes.choices(),
        null=False,
        blank=False,
        verbose_name='Type',
    )

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=[
            validators.MinLengthValidator(MIN_LENGTH_NAME),
            validate_plant_name,
        ],
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )

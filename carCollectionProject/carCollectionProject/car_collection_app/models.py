from enum import Enum

from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


class Profile(models.Model):
    MAX_LENGTH_USERNAME = 10
    MIN_LENGTH_USERNAME = 2
    MIN_AGE = 18
    MAX_LENGTH_PASSWORD = 30
    MAX_LENGTH_NAME = 30

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=[
            validators.MinLengthValidator(MIN_LENGTH_USERNAME, "The username must be a minimum of 2 chars"),
        ],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=[
            validators.MinValueValidator(MIN_AGE),
        ],
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_LENGTH_PASSWORD,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class CarTypes(Enum):
    SPORT_CAR = "Sport Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return [(x.value, x.value) for x in cls]


def validate_year(value):
    if not 1980 <= value <= 2049:
        raise ValidationError("Year must be between 1980 and 2049")


class Car(models.Model):
    class Meta:
        ordering = ('pk',)

    MAX_LENGTH_TYPE = 10
    MAX_LENGTH_MODEL = 20
    MIN_LENGTH_MODEL = 2
    MIN_PRICE = 1

    type = models.CharField(
        max_length=MAX_LENGTH_TYPE,
        choices=CarTypes.choices(),
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MAX_LENGTH_MODEL,
        validators=[
            validators.MinLengthValidator(MIN_LENGTH_MODEL),
        ],
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        validators=[
            validate_year,
        ],
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    price = models.FloatField(
        validators=[
            validators.MinValueValidator(MIN_PRICE),
        ],
        null=False,
        blank=False,
    )

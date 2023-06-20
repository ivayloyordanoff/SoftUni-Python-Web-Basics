from enum import Enum

from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def username_validator(value):
    for char in value:
        if not char.isalnum() and char != '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    MIN_LENGTH_USERNAME = 2
    MAX_LENGTH_USERNAME = 15

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=[validators.MinLengthValidator(MIN_LENGTH_USERNAME),
                    username_validator,
                    ],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class AlbumGenres(Enum):
    POP = "Pop Music"
    JAZZ = "Jazz Music"
    RNB = "R&B Music"
    ROCK = "Rock Music"
    COUNTRY = "Country Music"
    DANCE = "Dance Music"
    HIP_HOP = "Hip Hop Music"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class Album(models.Model):
    class Meta:
        ordering = ('pk',)

    MAX_LENGTH_ALBUM_NAME = 30
    MAX_LENGTH_ARTIST = 30
    MAX_LENGTH_GENRE = 30

    album_name = models.CharField(
        max_length=MAX_LENGTH_ALBUM_NAME,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Album Name'
    )

    artist = models.CharField(
        max_length=MAX_LENGTH_ARTIST,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_LENGTH_GENRE,
        choices=AlbumGenres.choices(),
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )

    price = models.FloatField(
        validators=[
            validators.MinValueValidator(0.0),
        ],
        null=False,
        blank=False,
    )

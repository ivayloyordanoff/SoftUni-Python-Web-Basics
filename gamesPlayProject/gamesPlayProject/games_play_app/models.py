from enum import Enum

from django.core import validators
from django.db import models


class ProfileModel(models.Model):
    MIN_AGE = 12
    MAX_LENGTH_PASSWORD = 30
    MAX_LENGTH_NAME = 30

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
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=True,
        blank=True,
        verbose_name='Last Name',
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture',
    )


class Categories(Enum):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    PUZZLE = "Puzzle"
    STRATEGY = "Strategy"
    SPORTS = "Sports"
    BOARD_CARD_GAME = "Board/Card Game"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return [(x.value, x.value) for x in cls]


class GameModel(models.Model):
    class Meta:
        ordering = ('pk',)

    MAX_LENGTH_TITLE = 30
    MAX_LENGTH_CATEGORY = 15
    MIN_RATING = 0.1
    MAX_RATING = 5.0
    MIN_MAX_LEVEL = 1

    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,
        unique=True,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=MAX_LENGTH_CATEGORY,
        choices=Categories.choices(),
        null=False,
        blank=False,
    )

    rating = models.FloatField(
        validators=[
            validators.MinValueValidator(MIN_RATING),
            validators.MaxValueValidator(MAX_RATING),
        ],
        null=False,
        blank=False,
    )

    max_level = models.IntegerField(
        validators=[
            validators.MinValueValidator(MIN_MAX_LEVEL),
        ],
        null=True,
        blank=True,
        verbose_name='Max Level',
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )

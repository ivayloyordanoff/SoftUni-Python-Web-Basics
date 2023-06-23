from django.db import models


class Profile(models.Model):
    MAX_LENGTH_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        verbose_name='Last Name',
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )


class Book(models.Model):
    MAX_LENGTH_TITLE = 30
    MAX_LENGTH_TYPE = 30

    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,
    )

    description = models.TextField()

    image = models.URLField()

    type = models.CharField(
        max_length=MAX_LENGTH_TYPE,
    )

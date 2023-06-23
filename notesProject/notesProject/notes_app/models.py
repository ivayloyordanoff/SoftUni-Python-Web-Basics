from django.db import models


class Profile(models.Model):
    MAX_LENGTH_NAME = 20

    first_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        verbose_name='Last Name',
    )

    age = models.IntegerField()

    image_url = models.URLField(
        verbose_name='Link to Profile Image',
    )


class Note(models.Model):
    class Meta:
        ordering = ('pk',)

    MAX_LENGTH_TITLE = 30

    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,
    )

    image_url = models.URLField(
        verbose_name='Link to Image',
    )

    content = models.TextField()

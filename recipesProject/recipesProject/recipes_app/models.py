from django.db import models


class Recipe(models.Model):
    class Meta:
        ordering = ('pk',)

    MAX_LENGTH_TITLE = 30
    MAX_LENGTH_INGREDIENTS = 250

    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )

    description = models.TextField()

    ingredients = models.CharField(
        max_length=MAX_LENGTH_INGREDIENTS,
    )

    time = models.IntegerField(
        verbose_name='Time (Minutes)',
    )

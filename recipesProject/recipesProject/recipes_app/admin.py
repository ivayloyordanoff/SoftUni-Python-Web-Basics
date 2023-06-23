from django.contrib import admin

from recipesProject.recipes_app.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass

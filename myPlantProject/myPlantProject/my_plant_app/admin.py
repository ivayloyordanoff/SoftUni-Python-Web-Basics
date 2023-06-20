from django.contrib import admin

from myPlantProject.my_plant_app.models import ProfileModel, PlantModel


@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    pass


@admin.register(PlantModel)
class PlantModelAdmin(admin.ModelAdmin):
    pass

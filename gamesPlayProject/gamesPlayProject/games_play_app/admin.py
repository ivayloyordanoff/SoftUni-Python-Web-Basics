from django.contrib import admin

from gamesPlayProject.games_play_app.models import ProfileModel, GameModel


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(GameModel)
class GameAdmin(admin.ModelAdmin):
    pass

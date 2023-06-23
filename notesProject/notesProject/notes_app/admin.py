from django.contrib import admin

from notesProject.notes_app.models import Profile, Note


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass

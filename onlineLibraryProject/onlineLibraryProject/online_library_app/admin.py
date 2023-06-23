from django.contrib import admin

from onlineLibraryProject.online_library_app.models import Profile, Book


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

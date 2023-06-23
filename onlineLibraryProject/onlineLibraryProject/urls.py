from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('onlineLibraryProject.online_library_app.urls')),
]

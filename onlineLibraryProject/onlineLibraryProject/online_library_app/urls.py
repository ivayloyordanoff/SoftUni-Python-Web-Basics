from django.urls import path, include

from onlineLibraryProject.online_library_app.views import index, book_add, book_edit, book_details, \
    profile, profile_edit, profile_delete, book_delete

urlpatterns = [
    path('', index, name='index'),
    path('add/', book_add, name='book add'),
    path('edit/<int:pk>/', book_edit, name='book edit'),
    path('details/<int:pk>/', book_details, name='book details'),
    path('delete/<int:pk>/', book_delete, name='book delete'),
    path('profile/', include([
        path('', profile, name='profile'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ])),
]

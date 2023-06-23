from django.shortcuts import render, redirect

from onlineLibraryProject.online_library_app.forms import ProfileCreateForm, BookCreateForm, BookDeleteForm, \
    BookEditForm, ProfileEditForm, ProfileDeleteForm
from onlineLibraryProject.online_library_app.models import Profile, Book


def get_profile():
    try:
        return Profile.objects.first()
    except Profile.DoesNotExist:
        return None


def add_profile(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def index(request):
    profile = get_profile()

    if profile is None:
        return add_profile(request)

    books = Book.objects.all()

    context = {
        'books': books,
        'profile': profile,
    }

    return render(request, 'home-with-profile.html', context)


def book_add(request):
    profile = get_profile()

    if request.method == 'GET':
        form = BookCreateForm()
    else:
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'add-book.html', context)


def book_edit(request, pk):
    profile = get_profile()
    book = Book.objects.get(pk=pk)

    if request.method == 'GET':
        form = BookEditForm(instance=book)
    else:
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'book': book,
        'profile': profile,
    }
    return render(request, 'edit-book.html', context)


def book_details(request, pk):
    profile = get_profile()
    book = Book.objects.get(pk=pk)

    context = {
        'book': book,
        'profile': profile,
    }
    return render(request, 'book-details.html', context)


def book_delete(request, pk):
    profile = get_profile()
    book = Book.objects.get(pk=pk)

    if request.method == 'GET':
        form = BookDeleteForm(instance=book)
    else:
        form = BookDeleteForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'book': book,
        'profile': profile,
    }
    return render(request, 'delete-book.html', context)


def profile(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'delete-profile.html', context)

from django.shortcuts import render, redirect

from notesProject.notes_app.forms import ProfileCreateForm, NoteCreateForm, NoteEditForm, NoteDeleteForm, \
    ProfileDeleteForm
from notesProject.notes_app.models import Note, Profile


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

    notes = Note.objects.all()

    context = {
        'notes': notes,
        'profile': profile,
    }

    return render(request, 'home-with-profile.html', context)


def note_add(request):
    profile = get_profile()

    if request.method == 'GET':
        form = NoteCreateForm()
    else:
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'note-create.html', context)


def note_edit(request, pk):
    profile = get_profile()
    note = Note.objects.get(pk=pk)

    if request.method == 'GET':
        form = NoteEditForm(instance=note)
    else:
        form = NoteEditForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'note': note,
        'profile': profile,
    }
    return render(request, 'note-edit.html', context)


def note_delete(request, pk):
    profile = get_profile()
    note = Note.objects.get(pk=pk)

    if request.method == 'GET':
        form = NoteDeleteForm(instance=note)
    else:
        form = NoteDeleteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'note': note,
        'profile': profile,
    }
    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    profile = get_profile()
    note = Note.objects.get(pk=pk)

    context = {
        'note': note,
        'profile': profile,
    }
    return render(request, 'note-details.html', context)


def profile(request):
    profile = get_profile()
    notes_count = Note.objects.count()

    context = {
        'profile': profile,
        'notes_count': notes_count
    }
    return render(request, 'profile.html', context)


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

    return render(request, 'profile-delete.html', context)

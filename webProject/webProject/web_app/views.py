from django.shortcuts import render, redirect

from webProject.web_app.forms import ProfileCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from webProject.web_app.models import ProfileModel, FruitModel


def get_profile():
    try:
        return ProfileModel.objects.first()
    except ProfileModel.DoesNotExist:
        return None


def no_profile(request):
    return render(request, 'index.html')


def index(request):
    profile = get_profile()

    if profile is None:
        return no_profile(request)

    context = {
        'profile': profile,
    }

    return render(request, 'index.html', context)


def dashboard(request):
    profile = get_profile()
    fruits = FruitModel.objects.all()

    context = {
        'fruits': fruits,
        'profile': profile,
    }
    return render(request, 'dashboard.html', context)


def fruit_create(request):
    profile = get_profile()

    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'create-fruit.html', context)


def fruit_details(request, pk):
    profile = get_profile()
    fruit = FruitModel.objects.get(pk=pk)

    context = {
        'fruit': fruit,
        'profile': profile,
    }

    return render(request, 'details-fruit.html', context)


def fruit_edit(request, pk):
    profile = get_profile()
    fruit = FruitModel.objects.get(pk=pk)

    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
        'profile': profile,
    }

    return render(request, 'edit-fruit.html', context)


def fruit_delete(request, pk):
    profile = get_profile()
    fruit = FruitModel.objects.get(pk=pk)

    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruit)
    else:
        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
        'profile': profile,
    }

    return render(request, 'delete-fruit.html', context)


def profile_create(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    posts_count = FruitModel.objects.count()

    context = {
        'profile': profile,
        'posts_count': posts_count,
    }

    return render(request, 'details-profile.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

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

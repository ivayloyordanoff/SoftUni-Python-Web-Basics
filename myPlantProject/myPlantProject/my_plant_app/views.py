from django.shortcuts import render, redirect

from myPlantProject.my_plant_app.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from myPlantProject.my_plant_app.models import ProfileModel, PlantModel


def get_profile():
    try:
        return ProfileModel.objects.first()
    except ProfileModel.DoesNotExist:
        return None


def no_profile(request):
    return render(request, 'home-page.html')


def index(request):
    profile = get_profile()

    if profile is None:
        return no_profile(request)

    context = {
        'profile': profile,
    }
    return render(request, 'home-page.html', context)


def catalogue(request):
    profile = get_profile()
    plants = PlantModel.objects.all()

    context = {
        'profile': profile,
        'plants': plants,
    }

    return render(request, 'catalogue.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    plants_count = PlantModel.objects.count()

    context = {
        'profile': profile,
        'plants_count': plants_count,
    }

    return render(request, 'profile-details.html', context)


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


def plant_create(request):
    profile = get_profile()

    if request.method == 'GET':
        form = PlantCreateForm()
    else:
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'create-plant.html', context)


def plant_details(request, pk):
    profile = get_profile()
    plant = PlantModel.objects.get(pk=pk)

    context = {
        'plant': plant,
        'profile': profile,
    }

    return render(request, 'plant-details.html', context)


def plant_edit(request, pk):
    profile = get_profile()
    plant = PlantModel.objects.get(pk=pk)

    if request.method == 'GET':
        form = PlantEditForm(instance=plant)
    else:
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
        'profile': profile,
    }

    return render(request, 'edit-plant.html', context)


def plant_delete(request, pk):
    profile = get_profile()
    plant = PlantModel.objects.get(pk=pk)

    if request.method == 'GET':
        form = PlantDeleteForm(instance=plant)
    else:
        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
        'profile': profile,
    }

    return render(request, 'delete-plant.html', context)

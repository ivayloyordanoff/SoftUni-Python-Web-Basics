from django.shortcuts import render, redirect

from carCollectionProject.car_collection_app.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from carCollectionProject.car_collection_app.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.first()
    except Profile.DoesNotExist:
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


def catalogue(request):
    profile = get_profile()
    cars = Car.objects.all()
    cars_count = Car.objects.count()

    context = {
        'profile': profile,
        'cars': cars,
        'cars_count': cars_count,
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

    return render(request, 'profile-create.html', context)


def profile_details(request):
    profile = get_profile()
    total_price_cars = 0

    for car in Car.objects.all():
        total_price_cars += car.price

    context = {
        'profile': profile,
        'total_cars_price': total_price_cars,
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

    return render(request, 'profile-edit.html', context)


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


def car_create(request):
    profile = get_profile()

    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'car-create.html', context)


def car_details(request, pk):
    profile = get_profile()
    car = Car.objects.get(pk=pk)

    context = {
        'car': car,
        'profile': profile,
    }

    return render(request, 'car-details.html', context)


def car_edit(request, pk):
    profile = get_profile()
    car = Car.objects.get(pk=pk)

    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
        'profile': profile,
    }

    return render(request, 'car-edit.html', context)


def car_delete(request, pk):
    profile = get_profile()
    car = Car.objects.get(pk=pk)

    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
        'profile': profile,
    }

    return render(request, 'car-delete.html', context)

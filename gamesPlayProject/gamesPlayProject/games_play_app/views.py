from django.shortcuts import render, redirect

from gamesPlayProject.games_play_app.forms import ProfileCreateForm, GameCreateForm, GameEditForm, GameDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from gamesPlayProject.games_play_app.models import ProfileModel, GameModel


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


def dashboard(request):
    profile = get_profile()
    games = GameModel.objects.all()

    context = {
        'profile': profile,
        'games': games,
    }

    return render(request, 'dashboard.html', context)


def profile_create(request):
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

    return render(request, 'create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    total_games = GameModel.objects.count()
    total_rating = 0
    average_rating = 0

    if total_games > 0:
        for game in GameModel.objects.all():
            total_rating += game.rating
            average_rating = total_rating / total_games

    context = {
        'profile': profile,
        'total_games': total_games,
        'average_rating': average_rating,
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


def game_create(request):
    profile = get_profile()

    if request.method == 'GET':
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'create-game.html', context)


def game_details(request, pk):
    profile = get_profile()
    game = GameModel.objects.get(pk=pk)

    context = {
        'game': game,
        'profile': profile,
    }

    return render(request, 'details-game.html', context)


def game_edit(request, pk):
    profile = get_profile()
    game = GameModel.objects.get(pk=pk)

    if request.method == 'GET':
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game,
        'profile': profile,
    }

    return render(request, 'edit-game.html', context)


def game_delete(request, pk):
    profile = get_profile()
    game = GameModel.objects.get(pk=pk)

    if request.method == 'GET':
        form = GameDeleteForm(instance=game)
    else:
        form = GameDeleteForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game,
        'profile': profile,
    }

    return render(request, 'delete-game.html', context)

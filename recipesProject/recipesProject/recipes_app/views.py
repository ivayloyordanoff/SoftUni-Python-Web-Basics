from django.shortcuts import render, redirect

from recipesProject.recipes_app.forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm
from recipesProject.recipes_app.models import Recipe


def index(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, 'index.html', context)


def create(request):
    if request.method == 'GET':
        form = RecipeCreateForm()
    else:
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)


def edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'GET':
        form = RecipeEditForm(instance=recipe)
    else:
        form = RecipeEditForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'recipe': recipe,
        'form': form
    }

    return render(request, 'edit.html', context)


def delete(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'GET':
        form = RecipeDeleteForm(instance=recipe)
    else:
        form = RecipeDeleteForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'delete.html', context)


def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(',')

    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }

    return render(request, 'details.html', context)

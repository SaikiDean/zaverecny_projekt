from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone


kategorie = Cat.objects.order_by("Cat_Name")[:7]
recepty = Recipe.objects.filter(Recipe_Date__lte=timezone.now()).order_by('-Recipe_Date')


def index(request):
    return render(request, '../templates/main.html', {'recipes': recepty, 'categories': kategorie})


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')


def profile(request):
    return render(request, "../templates/profile.html", {'categories': kategorie})


def add_cat(request):
    if request.method == "POST":
        form = AddCatForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('/catlist', pk=category.pk)
    else:
        form = AddCatForm()
    return render(request, '../templates/addcat.html', {'form': form, 'categories': kategorie})

def recipe_add(request):
    cats = Cat.objects.order_by("Cat_Name")
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.Recipe_Author = request.user
            recipe.save()
            return redirect('/details', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, '../templates/novy_recept.html', {'form': form, 'categories': kategorie, 'cats': cats})


def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, '../templates/details.html', {'recipe': recipe, 'categories': kategorie})


def cat_details(request, pk):
    category = get_object_or_404(Cat, pk=pk)
    return render(request, '../templates/cat_details.html',
                  {'recipes': recepty, 'category': category, 'categories': kategorie})


def cat_list(request):
    cats = Cat.objects.order_by("Cat_Name")
    return render(request, '../templates/catlist.html', {'categories': kategorie, 'cats': cats})


def recipe_list(request):
    return render(request, '../templates/recipe_list.html', {'recipes': recepty, 'categories': kategorie})


def registrace(request):
    if request.method == "POST":
        form = RegistraceForm(request.POST)
        jmeno = request.POST.get('username')
        heslo = request.POST.get('password1')
        if form.is_valid():
            osoba = form.save()
            uzivatel = authenticate(username=jmeno, password=heslo)
            osoba.save()
            login(request, uzivatel)
            return redirect('/')
    else:
        form = RegistraceForm()
    return render(request, '../templates/register.html', {'form': form, 'categories': kategorie})


def prihlaseni(request):
    if request.method == 'POST':
        form = PrihlaseniForm(request, request.POST)
        jmeno = request.POST.get('username')
        heslo = request.POST.get('password')
        if form.is_valid:
            osoba = authenticate(username=jmeno, password=heslo)
            login(request, osoba)
            return redirect('/')
    else:
        form = PrihlaseniForm()
    return render(request, '../templates/login.html', {'form': form, 'categories': kategorie})

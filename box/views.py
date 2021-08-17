from django.shortcuts import render, HttpResponseRedirect, reverse
from box.models import Recipe, Author
from box.forms import AddRecipeForm, AddAuthorForm
# Create your views here.


def index_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})


def author_detail(request, id):
    author = Author.objects.get(id=id)
    recipes = Recipe.objects.filter(author=author)
    return render(request, 'author_detail.html', {'author': author, 'recipes': recipes})


def addauthor(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))
    form = AddAuthorForm()
    return render(request, 'generic_form.html', {'form': form})


def addrecipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe = Recipe.objects.create(title=data['title'], author=data['author'],
            description=data['description'], time_required=data['time_required'],
            instructions=data['instructions'])
            return HttpResponseRedirect(reverse('homepage'))
    form = AddRecipeForm()
    return render(request, 'generic_form.html', {'form': form})

from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse, redirect
from box.models import Recipe, Author
from box.forms import AddRecipeForm, AddAuthorForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
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

@login_required
def addauthor(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            author = Author.objects.create(name=data['name'], bio=data['bio'])

            return HttpResponseRedirect(reverse('home'))

    form = AddAuthorForm()
    return render(request, 'generic_form.html', {'form': form})

@login_required
def addrecipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            recipe = Recipe.objects.create(title=data['title'], author=data['author'],
                                           description=data['description'], time_required=data['time_required'],
                                           instructions=data['instructions'])
            return HttpResponseRedirect(reverse('home'))

    form = AddRecipeForm()
    return render(request, 'generic_form.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('home')))
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return request(redirect('/home'))

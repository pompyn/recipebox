from django.contrib import admin

# Register your models here.
from box.models import Author, Recipe
# Register your models here.
admin.site.register(Author)
admin.site.register(Recipe)

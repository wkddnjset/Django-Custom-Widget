from django.contrib import admin
from .models import *
from .forms import CountryForm, PostForm
# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    form = CountryForm

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Recipe


def home(request):
    latest_recipe_list = Recipe.objects.order_by('-pub_date')[:5]
    output = ', '.join([r.recipe_name for r in latest_recipe_list])
    return HttpResponse(output)


def detail(request, recipe_id):
    return HttpResponse("It is recipe %s." % recipe_id)


def edit(request, recipe_id):
    return HttpResponse("You're editing on recipe %s." % recipe_id)

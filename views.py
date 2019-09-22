from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Recipe
#from django.template import loader
from django.shortcuts import render, get_object_or_404
#from django.http import Http404


def home(request):
    latest_recipe_list = Recipe.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('myapp/home.html')
    context = {
        'latest_recipe_list':latest_recipe_list,
    }
    #output = ', '.join([r.recipe_name for r in latest_recipe_list])
    #return HttpResponse(template.render(context,request))
    return render(request, 'myapp/home.html', context)



def detail(request, recipe_id):
    #try:
    #    r=Recipe.objects.get(pk=recipe_id)
    #except Recipe.DoesNotExist:
    #    raise Http404("Recipe does not extist.")
    r=get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'myapp/detail.html',{'recipe':r})

    #return HttpResponse("It is recipe %s." % recipe_id)


def edit(request, recipe_id):
    return HttpResponse("You're editing on recipe %s." % recipe_id)

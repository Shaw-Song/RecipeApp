from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    recipe_discription = models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.recipe_name
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=200)
    ingredient_quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.ingredient_name
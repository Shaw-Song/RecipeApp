from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:recipe_id>/', views.detail, name='detail'),
    path('<int:recipe_id>/edit/', views.edit, name='edit'),
]

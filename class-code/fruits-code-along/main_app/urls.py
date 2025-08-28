from django.urls import path
from . import views


urlpatterns = [
    path('welcome/', views.welcome),
    path('fruits/',views.all_fruits),
   
]

from django.urls import path
from . import views


urlpatterns = [
    path('welcome/', views.welcome),
    path('fruits/',views.all_fruits),
    path('fruits/<int:id>', views.fruit_details)
   
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('fruits/',views.all_fruits, name='fruit-list'),
    path('fruits/<int:id>/', views.fruit_details, name='fruit-detail'),
    path('fruits/create/',views.fruit_create, name='fruit-create'),
    path('fruits/<int:id>/edit/', views.fruit_update, name='fruit-update'),
    path('fruits/<int:id>/delete/', views.fruit_delete, name='fruit-delete'),

   
]

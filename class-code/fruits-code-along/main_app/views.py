from django.shortcuts import render
from .models import Fruit

# Create your views here.

def welcome(request):
    
    students = ['ali','mohammad','malak','maryam']
    return render(request,'welcome.html',{'name':'Jamal', 'students':students, 'is_logged_in':False})

# 1. create the view function
# 2. add the view function to your urls.py
# 3. create the html file


# GET for all the fruits
def all_fruits(request):

    # SELECT * FROM fruits
    fruits = Fruit.objects.all()
    return render(request,'fruits/fruit-list.html',{'fruits':fruits})


# GET for 1 fruit
def fruit_details(request,id):
    found_fruit = Fruit.objects.get(id=id)
    return render(request, 'fruits/fruit-detail.html',{'found_fruit':found_fruit})
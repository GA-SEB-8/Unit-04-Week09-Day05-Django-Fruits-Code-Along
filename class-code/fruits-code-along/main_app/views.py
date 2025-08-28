from django.shortcuts import render

# Create your views here.

def welcome(request):
    
    students = ['ali','mohammad','malak','maryam']
    return render(request,'welcome.html',{'name':'Jamal', 'students':students, 'is_logged_in':False})

# 1. create the view function
# 2. add the view function to your urls.py
# 3. create the html file


def all_fruits(request):

    return render(request,'fruit-list.html')
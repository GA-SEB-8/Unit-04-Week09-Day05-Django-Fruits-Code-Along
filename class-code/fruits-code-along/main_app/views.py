from django.shortcuts import render, redirect
from .models import Fruit
from .forms import FruitForm

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


# POST create 1 fruit
def fruit_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        is_ready_to_eat = request.POST.get('is_ready_to_eat') == "on"

        print(name)
        print(is_ready_to_eat)

        

        created_fruit = Fruit.objects.create(name = name, is_ready_to_eat = is_ready_to_eat )
        return redirect('fruit-list')


    return render(request,'fruits/fruit-form.html')



def fruit_update(request,id):
    fruit = Fruit.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        is_ready_to_eat = request.POST.get('is_ready_to_eat') == "on"
        
        # updating fruit information
        fruit.name = name
        fruit.is_ready_to_eat = is_ready_to_eat
        fruit.save()

        return redirect('fruit-list')



    return render(request, 'fruits/fruit-form.html', {'fruit':fruit})


def fruit_delete(request,id):

    Fruit.objects.get(id=id).delete()
    return redirect('fruit-list')




# Create with form

def fruit_create_with_form(request):
    if request.method == "POST":
        form = FruitForm(request.POST) # create a new fruit form instance with the data from the request

        if form.is_valid(): #validate the fruit form instance
            fruit = form.save()
            return redirect('fruit-list')

    form = FruitForm()
    return render(request,'fruits/fruit-form.html', {'form':form})


def update_fruit_form(request,id):
    fruit = Fruit.objects.get( id=id)
    if request.method == "POST":
        form = FruitForm(request.POST, instance=fruit)
        if form.is_valid():
            fruit = form.save()
            return redirect("fruit-list")
    else:
        form = FruitForm(instance=fruit)
    return render(request, "fruits/fruit_form.html", {"form": form, "mode": "Update"})






# Class Based Views (CBV)
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class FruitListView(ListView):
    model = Fruit
    template_name = 'fruits/fruit-list.html'
    context_object_name = 'fruits'
    queryset = Fruit.objects.filter(is_ready_to_eat = True)

 



class FruitCreateView(CreateView):
    model = Fruit
    fields = ['name','is_ready_to_eat']
    template_name = 'fruits/fruit-form.html'
    success_url = 'fruit-list'


class FruitDetailView(DetailView):
    model = Fruit
    template_name='fruits/fruit-detail.html'
    context_object_name = 'found_fruit'

class FruitUpdateView(UpdateView):
    model = Fruit
    fields = ['name','is_ready_to_eat']
    template_name = 'fruits/fruit-form.html'
    success_url = 'fruit-list'

class FruitDeleteView(DeleteView):
    model = Fruit
    success_url = 'fruit-list'

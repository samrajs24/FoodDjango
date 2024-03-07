from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import food_item
from django.template import loader
from .forms import FoodForm
from django.views.generic.list import ListView
# Create your views here.

def index(request):
    food_list = food_item.objects.all()
    #template = loader.get_template('food/index.html')
    context = {
        'food_list':food_list,
    }
    #return HttpResponse(template.render(context,request))
    return render(request,'food/index.html',context)

class IndexClassView(ListView):
    model = food_item;
    template_name = 'food/index.html'
    context_object_name = 'food_list'

def food_app_click(request):
    return render(request,'food/index.html')

def foods(request):
    return HttpResponse('<h2>This is a food item view</h2>')

def detail(request, food_item_id):
    food_id = food_item.objects.get(pk=food_item_id)
    context = {
        'food_id':food_id,
    }
    return render(request,'food/detail.html',context)

def add_food(request):
    form = FoodForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/food-form.html',{'form':form})

def update_food(request,id):
    food_id = food_item.objects.get(id=id)
    form = FoodForm(request.POST or None, instance=food_id)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/food-form.html',{'form':form,'food_id':food_id})

def delete_food(request,id):
    food_id = food_item.objects.get(id=id)

    if request.method == 'POST':
        food_id.delete()
        return redirect('food:index')
    
    return render(request,'food/food-delete.html',{'food_id':food_id})
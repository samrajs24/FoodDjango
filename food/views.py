from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import food_item
from django.template import loader
from .forms import FoodForm
# Create your views here.

def index(request):
    food_list = food_item.objects.all()
    #template = loader.get_template('food/index.html')
    context = {
        'food_list':food_list,
    }
    #return HttpResponse(template.render(context,request))
    return render(request,'food/index.html',context)

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
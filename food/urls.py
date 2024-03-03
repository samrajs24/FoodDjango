
from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('',views.index,name='index'),
    #/food/int
    path('<int:food_item_id>/',views.detail,name='detail'),
    path('foods/',views.foods,name='foods'),
    # add items
    path('add',views.add_food,name='add_food'),
]

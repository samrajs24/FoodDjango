
from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('',views.index,name='index'),
    path('',views.food_app_click,name='food_app_click'),
    #/food/int
    path('<int:food_item_id>/',views.detail,name='detail'),
    path('foods/',views.foods,name='foods'),
    # add items
    path('add',views.add_food,name='add_food'),
    # update items
    path('update/<int:id>/',views.update_food,name='update_food'),
    # delete items
    path('delete/<int:id>/',views.delete_food,name='delete_food'),
]

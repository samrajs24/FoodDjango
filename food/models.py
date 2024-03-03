from django.db import models

# Create your models here.
class food_item(models.Model):

    def __str__(self):
        return self.food_name

    food_name = models.CharField(max_length=200)
    food_desc = models.CharField(max_length=200)
    food_price = models.IntegerField()
    food_image = models.CharField(max_length=500,default="https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg")
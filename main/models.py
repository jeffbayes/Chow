from django.db import models

class Restaurant(models.Model):
    restaurant_id = models.CharField(max_length=40)
    restaurant_name = models.CharField(max_length=200)
    restaurant_cuisine = models.CharField(max_length=200)
    restaurant_price = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.restaurant_name


class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    menu_item_name = models.CharField(max_length=200)
    menu_item_description = models.CharField(max_length=5000)
    menu_item_price = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.menu_item_name

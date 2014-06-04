from django.contrib import admin
from main.models import DishEntry

class MenuInline(admin.StackedInline):
    model = DishEntry
    extra = 3

class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {
        'fields': ('restaurant_id', 'restaurant_cuisine', 'restaurant_price')
        }),
    ]
    inlines = [MenuInline]
    list_display = ('restaurant_id', 'restaurant_cuisine', 'restaurant_price')
    
# admin.site.register(Restaurant, RestaurantAdmin)

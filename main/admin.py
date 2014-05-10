from django.contrib import admin
from main.models import Restaurant, MenuItem

class MenuInline(admin.StackedInline):
    model = MenuItem
    extra = 3

class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {
        'fields': ('restaurant_name', 'restaurant_cuisine', 'restaurant_price')
        }),
    ]
    inlines = [MenuInline]
    list_display = ('restaurant_name', 'restaurant_cuisine', 'restaurant_price')
    
admin.site.register(Restaurant, RestaurantAdmin)

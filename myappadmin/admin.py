from django.contrib import admin
from .models import Customer, Product, Order

# admin.site.register(Customer)
# # admin.site.register(Product)
# admin.site.register(Order)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price',)
    search_fields = ('name',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity')
    list_filter = ('customer', 'product')
    search_fields = ('customer__name', 'product__name')

# admin.site.register(Customer, CustomerAdmin)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Order, OrderAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    fields = ('name', 'email')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price',)
    search_fields = ('name',)
    fields = ('name', 'price')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity')
    list_filter = ('customer', 'product')
    search_fields = ('customer__name', 'product__name')
    fields = ('customer', 'product', 'quantity')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

from django.contrib import admin

from products.models import Product

#changing view of admin panel for Product model
class ProductManager(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock',) # comma (,) is used because, it makes tuple
    list_filters = ('is_active',)
    search_fields = ('name',)
    # ordering = ("-id") #sorted using id in reverse order
    ordering = ("-created_at",)

# Register your models here.
admin.site.register(Product, ProductManager)
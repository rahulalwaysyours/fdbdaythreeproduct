from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True) #when new rows added
    updated_at = models.DateTimeField(auto_now=True) #when existing rows updated
    on_sale = models.BooleanField(default = False)


    #methods
    @property
    def tax(self):
        return self.price*0.3
    
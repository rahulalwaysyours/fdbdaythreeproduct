from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
def home(request):
    return render(request, 'home.html', {
        "a_list": [i for i in range(1,100)],
    })


#api as class not as function
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.filters import SearchFilter

# Create your views here.
def home(request):
    return render(request, 'home.html', {
        "a_list": [i for i in range(1,100)],
    })

def contact(request):
    return render(request, 'contact.html')


#api as class not as function
#Product List/Create
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    SearchFields = ['name', 'description']

#Product Update/Destroy
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    # we will reuse the same serializer
    serializer_class = ProductSerializer
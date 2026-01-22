from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response

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
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']
    ordering = ['-created_at']
    permission_classes = [IsAuthenticated]  # Only authenticated users can list and create

    def create(self, request, *args, **kwargs):
        # Only admins can create products
        if not request.user.is_staff:
            return Response(
                {'error': 'Only admin users can create products.'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # Automatically set is_active to True when creating
        serializer.save()


#Product Update/Destroy
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def update(self, request, *args, **kwargs):
        # Only admins can update products
        if not request.user.is_staff:
            return Response(
                {'error': 'Only admin users can update products.'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Only admins can delete products
        if not request.user.is_staff:
            return Response(
                {'error': 'Only admin users can delete products.'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)


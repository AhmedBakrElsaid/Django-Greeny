from itertools import product
from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView , DetailView

from .models import Category, Product , Brand
from django.db.models import Q,F 
from django.db.models.aggregates import Count,Min,Max,Sum,Avg
# Create your views here.

def product_list (request):
    products = Product.objects.select_related('category').select_related('brand').all()
    products = Product.objects.aggregate(Sum('quantity'))
    return render (request,'products/product_list_test.html',{'products':products})










class ProductList(ListView):
    model = Product
  
          
class ProductDetail(DetailView):
    model = Product
    
    
class BrandList(ListView):
    model = Brand
    
    def grt_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories']= Category.objects.all()
        return context
    
    
class BrandDetail(DetailView):
    model = Brand
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        context["brand_products"] =Product.objects.filter(brand = brand) 
        return context
    
class CategoryList(ListView):
    model = Category
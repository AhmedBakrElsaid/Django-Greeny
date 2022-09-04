from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView , DetailView

from .models import Category, Product , Brand
# Create your views here.

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
    
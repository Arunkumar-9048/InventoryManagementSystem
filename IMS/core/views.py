from django.shortcuts import render
from django.views.generic import *


# Create your views here.
class Index(TemplateView):
    template_name= 'index.html'
    
class Items(TemplateView):
    template_name= 'items.html'

class GoodsIn(TemplateView):
    template_name= 'goodsin.html'
    
class GoodsOut(TemplateView):
    template_name= 'goodsout.html'
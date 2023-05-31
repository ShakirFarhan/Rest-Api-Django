from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from products.models import Product
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer
@api_view(["GET"])
def home(request,*args,**kwargs):
    instance=Product.objects.all().order_by('?').last()
    data={}
    if instance:

        data=ProductSerializer(instance).data
        print(data)
    return Response(data)
    

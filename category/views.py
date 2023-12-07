from django.shortcuts import render
from rest_framework import generics
from .models import Categories
from .serializers import CategoryModelSerializer
# Create your views here.

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoryModelSerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoryModelSerializer

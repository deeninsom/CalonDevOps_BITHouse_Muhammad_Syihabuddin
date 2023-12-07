from django.shortcuts import render
from rest_framework import generics
from .models import Status
from .serializers import StatusModelSerializer

# Create your views here.
class StatusListCreateView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusModelSerializer

class StatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusModelSerializer
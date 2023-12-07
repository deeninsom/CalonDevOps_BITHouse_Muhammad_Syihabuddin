from rest_framework import serializers
from .models import Categories

class CategoryModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Categories
    fields = '__all__'

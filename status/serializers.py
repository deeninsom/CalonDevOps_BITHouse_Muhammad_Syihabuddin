from rest_framework import serializers
from .models import Status

class StatusModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Status
    fields = '__all__'
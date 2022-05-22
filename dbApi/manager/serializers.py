from rest_framework import serializers
from .models import Dx

class DxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dx
        fields = '__all__'


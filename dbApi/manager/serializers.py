from rest_framework import serializers
from .models import Dx, Px, Med, Lab, Fx, Event

class DxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dx
        fields = '__all__'

class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = '__all__'

class MedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Med
        fields = '__all__'

class PxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Px
        fields = '__all__'

class FxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fx
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
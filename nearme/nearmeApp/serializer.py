from rest_framework import serializers
from .models import Member

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

from rest_framework import serializers
from . models import UrlData

class UrlDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlData
        fields = '__all__'


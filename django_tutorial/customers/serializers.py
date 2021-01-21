from .models import *
from rest_framework import serializers


class CustomerTagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerTags
        fields = ['name']

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['name','phone','email','description','featured','tags']
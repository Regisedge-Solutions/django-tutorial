from .models import *
from rest_framework import serializers


class InteractionTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InteractionType
        fields = ['name']

class InteractionSubTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InteractionSubType
        fields = ['name','interaction_type']

class DispositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disposition
        fields = ['name']

class SubdispositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subdisposition
        fields = ['name','disposition']

class InteractionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interaction
        fields = ['id','customer','interaction_subtype','subdisposition','description','follow_up','follow_up_date','created_on','updated_on']

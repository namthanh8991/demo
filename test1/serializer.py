from rest_framework import serializers
from .models import Person
class PersonPortalserializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    age = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100 )
class Personserializer(serializers.ModelSerializer):
    class Meta:
        table = 'person'
        fields = ('name ', 'age', 'address')


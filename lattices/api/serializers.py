from rest_framework import serializers
from lattices.models import Lattices

class LatticesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lattices
        fields = '__all__'
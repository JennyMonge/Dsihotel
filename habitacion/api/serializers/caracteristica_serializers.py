from habitacion.models import Caracteristica
from rest_framework import serializers

class CaracteristicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caracteristica
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
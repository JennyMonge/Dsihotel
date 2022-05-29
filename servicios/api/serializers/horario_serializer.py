from servicios.models import Horarios
from rest_framework import serializers

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Horarios
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
from servicios.models import Servicios
from rest_framework import serializers


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

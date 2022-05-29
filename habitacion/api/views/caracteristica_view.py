from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from base.api import GeneralListApiView
from habitacion.api.serializers.caracteristica_serializers import *


class CaracteristicaViewSet(viewsets.ModelViewSet):
    serializer_class = CaracteristicaSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        caracteristica_serializer = self.get_serializer(
            self.get_queryset(), many=True)
        return Response(caracteristica_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Caracteristica creada correctamente!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            caracteristica_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)

            if caracteristica_serializer.is_valid():
                caracteristica_serializer.save()
                return Response(caracteristica_serializer.data, status=status.HTTP_200_OK)
            return Response(caracteristica_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        caracteristica = self.get_queryset().filter(id=pk).first()
        if caracteristica:
            caracteristica.state = False
            caracteristica.save()
            return Response({'message': 'Caracterisitica Eliminada correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe una caracteristica con esos datos'}, status=status.HTTP_400_BAD_REQUEST)

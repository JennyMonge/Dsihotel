from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from base.api import GeneralListApiView
from servicios.api.serializers.horario_serializer import *

class HorarioViewSet(viewsets.ModelViewSet):
    serializer_class = HorarioSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        horario_serializer=self.get_serializer(self.get_queryset(),many=True)
        return Response(horario_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Servicio creado correctamente!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            horario_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)

            if horario_serializer.is_valid():
                horario_serializer.save()
                return Response(horario_serializer.data, status=status.HTTP_200_OK)
            return Response(horario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        horario = self.get_queryset().filter(id=pk).first()
        if horario:
            horario.state = False
            horario.save()
            return Response({'message': 'Horario Eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un horario con esos datos'}, status=status.HTTP_400_BAD_REQUEST)

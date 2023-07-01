from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from .models import Tarea
from .serializers import TareaSerializer


class IndexView(APIView):
    def get(self, request):
        context = {
            'status': True,
            'content': 'servidor ativo'
        }
        
        return Response(context)
    
class TareaView(APIView):
    def get(self, request):
        # 1. Traemos todas las tareas de la DB
        data = Tarea.objects.all()
        # 2. TareaSerializer - Toma el query set y lo pasa a dict pera un registro o varios con many=True
        ser_data = TareaSerializer(data,many=True)
        # 3. Response enviara JSON como respuesta
        return Response(ser_data.data)
    
    def post(self, request):
        # 1. request.data nos traera los datos del body segun los atributos de la clase TareaSerializer (Deserealización)
        ser_data = TareaSerializer(data=request.data)
        # 2. Validamos la data
        ser_data.is_valid(raise_exception=True)
        # 3. Guardamos la data
        ser_data.save()
        
        return Response(ser_data.data)
    
# Clase especial para PUT y DELETE ya que requerimos obtener su ID
class TareaDetailView(APIView):
    
    def get_object(self, pk):
        try:
            return Tarea.objects.get(pk=pk)
        except Tarea.DoesNotExist:
            raise Http404
    # Get por ID
    def get(self, request, pk):
        data = self.get_object(pk)
        ser_data = TareaSerializer(data)
        return Response(ser_data.data)
    
    #PUT needs a ID
    def put(self, request, pk):
        # 1. Obtenemos el registro a actualizar
        data = self.get_object(pk)
        # 2. TareaSerializer(data_actual, data_a_actualizar) 
        ser_data = TareaSerializer(data, data=request.data)
        # 3. Validamos y guardamos
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        # 1. Obtenemos el registro a actualizar
        data = self.get_object(pk)
        # 2. Eliminamos
        data.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
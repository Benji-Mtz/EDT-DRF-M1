from rest_framework import serializers
from .models import Tarea

# La clase ModelSerializer servira para obtener los campos a partir del modelo de una clase
class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        # fields = ('campo_especifico1'...n)
        fields = '__all__'
        

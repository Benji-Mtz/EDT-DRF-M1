from rest_framework import serializers
from .models import Tarea

# La clase ModelSerializer servira para obtener los campos a partir del modelo de una clase
class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        # fields = ('campo_especifico1'...n)
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.estado == '1':
            estado = "pendiente"
        elif instance.estado == "2":
            estado = "terminado"
            
        representation['estado'] = estado
        
        return representation
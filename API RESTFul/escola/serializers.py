from rest_framework import serializers
from escola.models import Estudante,Curso,Matricula

# serializers: responsável por converter dados complexos (objetos de banco de dados, json, xml...)


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email','cpf','data_nascimento','celular']
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__' #outra forma
        
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = [] #Não está excluindo nada. (outro modo de fazer)
        
        
class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField() 
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo'] 
    def get_periodo(self,obj):
        return obj.get_periodo_display()
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer): # vai converter objetos do modelo Matricula para um formato JSON.
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome') #pegando a descrição do curso (curso.descricao) e torna-la somente leitura.
    class Meta: #classe que define quais campos vão ser incluidos na serialização
        model = Matricula
        fields = ['estudante_nome']
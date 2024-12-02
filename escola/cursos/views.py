from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializaer, AvaliacaoSerializar
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# =========================================== API V1 =================================================================================

class CursoAPIView(generics.RetrieveDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializaer

class CursosAPIView(generics.ListCreateAPIView):    
    queryset = Curso.objects.all()
    serializer_class = CursoSerializaer

class AvaliacaoAPIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializar

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id = self.kwargs.get('curso_pk'), pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk = self.kwargs.get('avaliacao_pk'))

class AvaliacoesAPIView (generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializar

    def get_queryset(self): # pega dados de uma listagem de objetos, mais de um no caso 
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id = self.kwargs.get('curso_pk'))
        return self.queryset.all()
        

# ========================================================== API V2 =================================================

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializaer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        curso = self.get_object()
        serializer = AvaliacaoSerializar(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)
    
# ViewSet Padrão
# class AvaliacaoViewSet(viewsets.ModelViewSet):
    # queryset = Avaliacao.objects.all()
    # serializer_class = AvaliacaoSerializar

#ViewSet Customizado 
class AvaliacaoViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializar

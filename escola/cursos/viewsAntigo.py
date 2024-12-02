# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Curso, Avaliacao
# from .serializers import CursoSerializaer, AvaliacaoSerializar

# class CursoAPIView(APIView):
#     def get(self, request):
#         cursos = Curso.objects.all()
#         serializer = CursoSerializaer(cursos, many= True)
#         return Response(serializer.data)


#     def post(self, request):
#         serializer = CursoSerializaer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
        

# class AvaliacaoAPIView(APIView):
#     def get(self, request):
#         avaliacoes = Avaliacao.objects.all()
#         serializer = AvaliacaoSerializar(avaliacoes, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = AvaliacaoSerializar(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
        
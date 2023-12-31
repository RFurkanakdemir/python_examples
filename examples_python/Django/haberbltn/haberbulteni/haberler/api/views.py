from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from haberler.models import Makale
from haberler.api.serializers import MakaleSerializer

#class viewss
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class MakaleListCreateAPIView(APIView):
    def get(self,request):
        makaleler = Makale.objects.all()
        serializer = MakaleSerializer(makaleler, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = MakaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class MakaleDetailAPIView(APIView):
    def get_objects(self,pk):
        makale_instance = get_object_or_404(Makale, pk=pk)
        return makale_instance

    def get(self,request,pk):
        makale = self.get_objects(pk=pk)
        serializer = MakaleSerializer(makale)
        return Response(serializer.data)


    def put(self,request,pk):
        makale=self.get_objects(pk=pk)
        serializer=MakaleSerializer(makale,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializstatus=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        makale=self.get_objects(pk=pk)
        makale.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET','POST'])
# def makale_list_create_api_view(request):

#     if request.method == 'GET':
#         makaleler = Makale.objects.all()
#         serializer = MakaleSerializer(makaleler, many=True)
#         return Response(serializer.data)


#     elif request.method == 'POST':
#         serializer = MakaleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','PUT','DELETE'])
# def makale_detail_api_view(request,pk):
#     try:
#         makale_instance=Makale.objects.get(pk=pk)
#     except Makale.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)




#     if request.method == 'GET':
#         serializer = MakaleSerializer(makale_instance)
#         return Response(serializer.data)


#     elif request.method == 'PUT':
#         serializer = MakaleSerializer(makale_instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
        
#     elif request.method == 'DELETE':
#         makale_instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

    




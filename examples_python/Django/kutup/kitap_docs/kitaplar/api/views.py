from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions

from kitaplar.api.serializers import KitapSerializer,YorumSerializer
from kitaplar.models import Kitap,Yorum
from kitaplar.api.permissions import IsAdminUserOrReadOnly,IsYorumSahibiOrReadOnly
from kitaplar.api.pagination import SmallPagination,LargePAgination

#concrete view
class KitapListCreateAPIView(generics.ListCreateAPIView):
    queryset=Kitap.objects.all().order_by('id')
    serializer_class=KitapSerializer
    #permissions
    permission_classes=[IsAdminUserOrReadOnly]
    #pagination
    pagination_class=SmallPagination


class KitapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Kitap.objects.all()
    serializer_class=KitapSerializer

class YorumCreateAPIView(generics.CreateAPIView):
    queryset=Yorum.objects.all()
    serializer_class=YorumSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        #path('kitaplar/<int:kitap_pk>/yorum_yap', api_views.YorumCreateAPIView.as_view(), name='yorum yap'),
        kitap_pk=self.kwargs.get('kitap_pk')
        kitap=get_object_or_404(Kitap,pk=kitap_pk)
        kullanici=self.request.user
        serializer.save(kitap=kitap,yorum_sahibi=kullanici)

class YorumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Yorum.objects.all()
    serializer_class=YorumSerializer
    permission_classes=[IsYorumSahibiOrReadOnly]



#Generic Viewss
# class KitapListCreateAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):

#     queryset=Kitap.objects.all()
#     serializer_class=KitapSerializer

#     #listeleme
#     def get(self,request,*args ,**kwargs):
#         return self.list(request, *args , **kwargs)

#     #oluşturma
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

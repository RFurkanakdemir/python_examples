from django.urls import path
from haberler.api import views as api_views

urlpatterns = [
    
    path('makaleler/', api_views.MakaleListCreateAPIView.as_view(), name="makale_listesi"),
    path('makaleler/<int:pk>', api_views.MakaleDetailAPIView.as_view(), name="makale_detay"),
]
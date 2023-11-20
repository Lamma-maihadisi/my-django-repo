from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from .serializers import MenuSerializer , BookingSerializer
from .models import MenuTable , Booking
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.



def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, RetrieveDestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
   
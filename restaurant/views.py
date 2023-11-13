from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from .serializers import MenuSerializer, BookingSerializer
from .models import MenuTable, BookingTable
from rest_framework.viewsets import ModelViewSet

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
    queryset = BookingTable.objects.all()
    serializer_class = BookingSerializer
   
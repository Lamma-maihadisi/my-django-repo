from rest_framework.serializers import ModelSerializer
from .models import MenuTable, BookingTable

class MenuSerializer(ModelSerializer):
    class Meta:
        model = MenuTable
        fields = '__all__'


class BookingSerializer(ModelSerializer):
    class Meta:
        model = BookingTable
        fields = '__all__'
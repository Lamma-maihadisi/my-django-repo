from rest_framework.serializers import ModelSerializer
from .models import MenuTable, Booking

class MenuSerializer(ModelSerializer):
    class Meta:
        model = MenuTable
        fields = '__all__'


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
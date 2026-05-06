from rest_framework import serializers
from .models import Park, Trail, Event, Availability, Waterfall, Biodiversity
class ParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = '__all__'


class TrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'

class WaterfallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waterfall
        fields = '__all__'


class BiodiversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Biodiversity
        fields = '__all__'
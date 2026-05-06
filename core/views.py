from django.shortcuts import render
from rest_framework import viewsets

from .models import Park, Trail, Event, Availability, Waterfall, Biodiversity

from .serializers import (
    ParkSerializer,
    TrailSerializer,
    EventSerializer,
    AvailabilitySerializer,
    WaterfallSerializer,
    BiodiversitySerializer
)


class ParkViewSet(viewsets.ModelViewSet):
    queryset = Park.objects.all()
    serializer_class = ParkSerializer


class TrailViewSet(viewsets.ModelViewSet):
    queryset = Trail.objects.all()
    serializer_class = TrailSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer


class WaterfallViewSet(viewsets.ModelViewSet):
    queryset = Waterfall.objects.all()
    serializer_class = WaterfallSerializer


class BiodiversityViewSet(viewsets.ModelViewSet):
    queryset = Biodiversity.objects.all()
    serializer_class = BiodiversitySerializer


def home(request):
    return render(request, 'core/home.html')


def parks_view(request):
    parks = Park.objects.all()

    for park in parks:
        park.availability = Availability.objects.filter(park=park).first()

    return render(request, 'core/parks.html', {'parks': parks})


def trails_view(request):
    trails = Trail.objects.all()
    return render(request, 'core/trails.html', {'trails': trails})


def events_view(request):
    events = Event.objects.all()
    return render(request, 'core/events.html', {'events': events})


def waterfalls_view(request):
    waterfalls = Waterfall.objects.all()
    return render(request, 'core/waterfalls.html', {'waterfalls': waterfalls})


def biodiversity_view(request):
    biodiversity = Biodiversity.objects.all()
    return render(request, 'core/biodiversity.html', {'biodiversity': biodiversity})


def park_detail(request, park_id):
    park = Park.objects.get(id=park_id)
    trails = Trail.objects.filter(park=park)

    return render(request, 'core/park_detail.html', {
        'park': park,
        'trails': trails
    })
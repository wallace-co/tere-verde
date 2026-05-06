from django.contrib import admin
from .models import Park, Trail, Event, Availability, Waterfall, Biodiversity

@admin.register(Park)
class ParkAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')
    fields = ('name', 'description', 'image')


@admin.register(Trail)
class TrailAdmin(admin.ModelAdmin):
    list_display = ('name', 'park', 'difficulty', 'length_km', 'duration_min', 'is_open')
    list_filter = ('park', 'difficulty', 'is_open')
    search_fields = ('name', 'description')
    fields = (
        'name',
        'park',
        'difficulty',
        'length_km',
        'duration_min',
        'description',
        'image',
        'is_open',
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'park', 'date', 'is_open')
    list_filter = ('park', 'is_open', 'date')
    search_fields = ('name', 'description')
    fields = (
        'name',
        'park',
        'date',
        'description',
        'image',
        'is_open',
    )


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('park', 'open_time', 'close_time', 'is_open')
    list_filter = ('park', 'is_open')
    fields = (
        'park',
        'open_time',
        'close_time',
        'is_open',
    )

    admin.site.register(Waterfall)
admin.site.register(Biodiversity)
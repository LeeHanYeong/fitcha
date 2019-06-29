from django.contrib import admin

from .models import (
    Gym,
    GymImage,
    Service,
    Facility,
)


class GymImageInline(admin.TabularInline):
    model = GymImage
    extra = 3


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1


@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'phone_number')
    inlines = [
        GymImageInline,
        ServiceInline,
    ]


@admin.register(GymImage)
class GymImageAdmin(admin.ModelAdmin):
    list_display = ('gym', 'img')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('type', 'cost', 'gym')
    list_filter = ('gym', 'type')


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    pass

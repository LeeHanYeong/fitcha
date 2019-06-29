from django.contrib import admin
from django.utils.html import format_html

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
    list_display = (
        'name', 'location', 'phone_number',
        'images', 'facilities', 'services',
    )
    inlines = [
        GymImageInline,
        ServiceInline,
    ]

    def images(self, obj):
        return format_html(
            ''.join([
                f'<img src="{image.img.url}" style="'
                f'max-width: 200px;'
                f'max-height: 200px;'
                f'margin-right: 10px;'
                f'border-radius: 5px;">'
                for image in obj.image_set.all()
            ]))
    images.short_description = '이미지 목록'

    def facilities(self, obj):
        return ', '.join([
            facility.name for facility in obj.facility_set.all()])

    facilities.short_description = '시설 목록'

    def services(self, obj):
        return format_html(
            '<br>'.join([
                '<div>{type} ({price:,}원)</div>'.format(
                    type=service.get_type_display(),
                    price=service.cost,
                ) for service in obj.service_set.all()
            ])
        )
    services.short_description = '서비스 목록'

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

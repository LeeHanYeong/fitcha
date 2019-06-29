from rest_framework import serializers

from .models import Gym, GymImage, Facility, Service


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = (
            'pk',
            'name',
        )


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'pk',
            'type',
            'cost',
        )


class GymImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymImage
        fields = (
            'pk',
            'img',
        )


class GymSerializer(serializers.ModelSerializer):
    image_set = GymImageSerializer(many=True)
    service_set = ServiceSerializer(many=True)
    facility_set = FacilitySerializer(many=True)

    class Meta:
        model = Gym
        fields = (
            'pk',
            'name',
            'location',
            'phone_number',
            'description',

            'image_set',
            'service_set',
            'facility_set',
        )

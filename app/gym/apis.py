from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

from .models import Gym
from .serializers import GymSerializer


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        operation_summary='Gym List',
        operation_description='GYM 목록'
    )
)
class GymListAPIView(generics.ListAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        operation_summary='Gym Retrieve',
        operation_description='GYM 정보'
    )
)
class GymRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer

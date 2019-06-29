from django.urls import path

from . import apis

app_name = 'gym'
urlpatterns = [
    path('', apis.GymListAPIView.as_view()),
    path('<int:pk>/', apis.GymRetrieveAPIView.as_view()),
]

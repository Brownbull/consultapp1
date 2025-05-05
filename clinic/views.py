# ruff: noqa: ERA001, E501
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Appointment
from .models import Doctor
from .models import Patient
from .serializers import AppointmentSerializer
from .serializers import DoctorSerializer
from .serializers import PatientSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["name", "specialty"]
    ordering_fields = ["name"]


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["name"]
    ordering_fields = ["name", "birth_date"]


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["doctor", "patient"]
    search_fields = ["notes"]
    ordering_fields = ["date"]
    permission_classes = [IsAuthenticated]

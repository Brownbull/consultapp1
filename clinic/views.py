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


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

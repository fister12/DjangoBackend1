from rest_framework import generics, mixins, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import PatientRecord, Department
from .serializers import PatientRecordSerializer, DepartmentSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class PatientRecordListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientRecordSerializer

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Doctors').exists():
            return PatientRecord.objects.filter(department__in=user.departments.all())
        return PatientRecord.objects.none()

class PatientRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Doctors').exists():
            return PatientRecord.objects.filter(department__in=user.departments.all())
        if user.groups.filter(name='Patients').exists():
            return PatientRecord.objects.filter(patient=user)
        return PatientRecord.objects.none()

# Define other views similarly...

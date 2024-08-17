from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.DepartmentListCreateView.as_view(), name='departments'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department-detail'),
    path('patient_records/', views.PatientRecordListCreateView.as_view(), name='patient-records'),
    path('patient_records/<int:pk>/', views.PatientRecordDetailView.as_view(), name='patient-record-detail'),
    # Define other URLs similarly...
]

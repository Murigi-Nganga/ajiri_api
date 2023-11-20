from rest_framework import generics
from job_applications.mixins import PartialUpdateMixin

from job_applications.serializers import (JobApplicationCreateViewSerializer, 
                                          JobApplicationListViewSerializer, 
                                          JobApplicationUpdateViewSerializer)

from .models import JobApplication

# Create your views here.
class JobApplicationListView(generics.ListAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationListViewSerializer
    
         
class JobApplicationCreateView(generics.CreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationCreateViewSerializer
    
    def perform_create(self, serializer):
        # Set the status to 'Applied' before saving the instance
        serializer.save(status='Applied')
        
class JobApplicationUpdateView(PartialUpdateMixin, generics.UpdateAPIView):
    queryset = JobApplication.objects.filter(status__in=['Under Review', 'Applied'])
    serializer_class = JobApplicationUpdateViewSerializer
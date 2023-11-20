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
    
class ApplicantJobApplicationListView(generics.ListAPIView):
    serializer_class = JobApplicationListViewSerializer

    def get_queryset(self):
        applicant_id = self.kwargs['applicant_id']
        print(applicant_id)
        
        # Filter job applications for the applicant
        queryset = JobApplication.objects.filter(applicant_id=applicant_id)
        return queryset
    
# class CompanyJobApplicationListView(generics.ListAPIView):
#     serializer_class = JobApplicationListViewSerializer

#     def get_queryset(self):
#         company_id = self.kwargs['company_name']
        
#         # Filter job applications for the applicant
#         queryset = JobApplication.objects.filter(job_company_id=company_id)
#         return queryset
    
         
class JobApplicationCreateView(generics.CreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationCreateViewSerializer
    
    def perform_create(self, serializer):
        # Set the status to 'Applied' before saving the instance
        serializer.save(status='Applied')
        
class JobApplicationUpdateView(PartialUpdateMixin, generics.UpdateAPIView):
    queryset = JobApplication.objects.filter(status__in=['Under Review', 'Applied'])
    serializer_class = JobApplicationUpdateViewSerializer
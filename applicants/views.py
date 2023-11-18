from rest_framework import generics

from applicants.models import Applicant
from applicants.serializers import ApplicantSerializer

# Create your views here.
class ApplicantListCreateView(generics.ListCreateAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    
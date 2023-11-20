from rest_framework import generics
from .models import Company
from .serializers import CompanySerializer

# Create your views here.

class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
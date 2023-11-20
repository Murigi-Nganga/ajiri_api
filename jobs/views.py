from rest_framework import generics, status
from rest_framework.response import Response

from jobs.models import Job
from jobs.serializers import JobSerializer

# Create your views here.
class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    
    def create(self, request, *args, **kwargs):
        # Adding a list of jobs
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Adding a single job
        else:
            return super().create(request, *args, **kwargs)
        

from rest_framework import serializers

from .models import JobApplication

class JobApplicationListCreateViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobApplication
        fields = '__all__'
        depth = 2
        read_only_fields = ['status']
        
class JobApplicationUpdateViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobApplication
        # Only allow updating of the status
        fields = ['status']
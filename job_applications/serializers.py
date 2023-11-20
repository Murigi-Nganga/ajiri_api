from rest_framework import serializers

from .models import JobApplication

class JobApplicationListViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobApplication
        fields = '__all__'
        depth = 1
        
class JobApplicationCreateViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobApplication
        fields = '__all__'
        read_only_fields = ['status']
        
class JobApplicationUpdateViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobApplication
        # Only allow updating of the status
        fields = ['status']
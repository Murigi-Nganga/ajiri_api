from rest_framework import serializers

from applicants.models import Applicant

class ApplicantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Applicant
        fields = "__all__"
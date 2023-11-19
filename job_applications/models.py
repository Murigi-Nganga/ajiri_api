from django.db import models

from applicants.models import Applicant
from jobs.models import Job

# Create your models here.
class JobApplication(models.Model):
    
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Under Review', 'Under Review'),
        ('Hired', 'Hired'),
        ('Rejected', 'Rejected'),
    ]
    
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Applied')
    
    # Ensure an applicant can apply for a specific job only once
    class Meta:
        unique_together = ('applicant', 'job')

    def __str__(self):
        return f"{self.applicant} applied for {self.job} - Status: {self.status}"
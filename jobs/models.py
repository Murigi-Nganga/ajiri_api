from django.db import models

from companies.models import Company

# Create your models here.
class Job(models.Model):
    position = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    requirements = models.TextField()
    
    class Meta:
        unique_together = ('position', 'company')
    
    def __str__(self):
        return f"{self.position} at {self.company}"
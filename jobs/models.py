from django.db import models

# Create your models here.
class Job(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    description = models.TextField()
    requirements = models.TextField()
    
    def __str__(self):
        return f"${self.position} position at ${self.company}"
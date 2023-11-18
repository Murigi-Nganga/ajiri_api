from django.db import models

# Create your models here.
class Applicant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    resume_file_path = models.CharField(max_length=300)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
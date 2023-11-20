import json
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from companies.models import Company

from jobs.models import Job

# Create your tests here.

class JobModelTest(TestCase):
    def test_job_creation(self):
        company = Company.objects.create(
            name="Test Company",
            description="Description of the company",
            location="Test Location"
        )
        
        job = Job.objects.create(
            position="Backend Developer",
            description="Develop and maintain software applications.",
            requirements="Bachelor's degree in Computer Science.",
            company=company
        )
        self.assertEqual(job.company.location, "Test Location")

class JobAPITest(APITestCase):
        
    def setUp(self):
        company = Company.objects.create(
            name="Test Company",
            description="Description of the company",
            location="Test Location"
        )
        Job.objects.create(
            position="Android Developer",
            description="Develop and maintain android applications.",
            requirements="2 years of Android Development Experience",
            company=company
        )
        Job.objects.create(
            position="Software Developer",
            description="Develop and maintain Software applications.",
            requirements="BSc in Computer Science, IT or any other related field",
            company=company
        )

    def test_job_list_view(self):
        response = self.client.get('/api/jobs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_single_job_view(self):
        company = Company.objects.first()
        data = {
            "position": "Data Scientist",
            "description": "Analyze and interpret complex data sets.",
            "requirements": "Master's degree in Statistics.",
            "company": company.id
        }
        response = self.client.post('/api/jobs/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Job.objects.count(), 3)

    def test_create_multiple_jobs_view(self):
        company = Company.objects.first()
        data = [
            {
                "position": "Project Manager",
                "description": "Drive projects.",
                "requirements": "Master's degree in Project Management.",
                "company": company.id
            },
            {
                "position": "Marketing Specialist",
                "description": "Create and implement marketing strategies.",
                "requirements": "Bachelor's degree in Marketing.",
                "company": company.id
            }
        ]
        response = self.client.post('/api/jobs/', json.dumps(data), 
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Job.objects.count(), 4)


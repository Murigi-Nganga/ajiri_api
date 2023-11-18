from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from jobs.models import Job

# Create your tests here.

class JobModelTest(TestCase):
    def test_job_creation(self):
        job = Job.objects.create(
            position="Backend Developer",
            description="Develop and maintain software applications.",
            requirements="Bachelor's degree in Computer Science.",
            company="I&M Bank"
        )
        self.assertEqual(str(job), "Backend Developer at I&M Bank")

class JobAPITest(APITestCase):
    def setUp(self):
        Job.objects.create(
            position="Android Developer",
            description="Develop and maintain android applications.",
            requirements="2 years of Android Development Experience",
            company="Safaricom"
        )

    def test_get_job_list(self):
        response = self.client.get('/api/jobs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_single_job(self):
        data = {
            "position": "Data Scientist",
            "description": "Analyze and interpret complex data sets.",
            "requirements": "Master's degree in Statistics.",
            "company": "Google"
        }
        response = self.client.post('/api/jobs/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Job.objects.count(), 2)

    def test_create_multiple_jobs(self):
        data = [
            {
                "position": "Data Scientist",
                "description": "Analyze and interpret complex data sets.",
                "requirements": "Master's degree in Statistics.",
                "company": "NCBA"
            },
            {
                "position": "Marketing Specialist",
                "description": "Create and implement marketing strategies.",
                "requirements": "Bachelor's degree in Marketing.",
                "company": "SokoPlus"
            }
        ]
        response = self.client.post('/api/jobs/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Job.objects.count(), 3)


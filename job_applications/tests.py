# Create your tests here.
from django.test import TestCase

from companies.models import Company
from .models import JobApplication, Applicant, Job

from rest_framework import status
from rest_framework.test import APITestCase


class JobApplicationModelTest(TestCase):

    def setUp(self):
        # Sample test data
        self.applicant = Applicant.objects.create(
            first_name='John',
            last_name='Doe',
            email='jdoe@gmail.com',
            phone_number='0722748949',
            resume='resume/my_resume.pdf'
        )
        self.company = Company.objects.create(
            name="Test Company",
            description="Description of the company",
            location="Test Location"
        )
        self.job = Job.objects.create(
            position='Software Developer',
            company=self.company,
            description='Job description',
            requirements='Requirements for the job'
        )

    def test_job_application_creation(self):
        job_application = JobApplication.objects.create(
            applicant=self.applicant,
            job=self.job,
        )
        self.assertEqual(job_application.applicant, self.applicant)
        self.assertEqual(job_application.job, self.job)
        self.assertEqual(job_application.status, 'Applied')

    def test_unique_together_constraint(self):
        # Ensure an applicant can apply for a specific job only once
        JobApplication.objects.create(
            applicant=self.applicant,
            job=self.job,
        )
        with self.assertRaises(Exception):
            JobApplication.objects.create(
                applicant=self.applicant,
                job=self.job,
            )


class JobApplicationViewAPITests(APITestCase):

    def setUp(self):
        # Create sample data for testing
        self.applicant = Applicant.objects.create(
            first_name='John',
            last_name='Doe',
            email='jdoe@gmail.com',
            phone_number='0789678456',
            resume='resume/my_resume.pdf'
        )
        self.company = Company.objects.create(
            name="Test Company",
            description="Description of the company",
            location="Test Location"
        )
        
        self.job = Job.objects.create(
            position='Software Developer',
            company=self.company,
            description='Description of the job',
            requirements='Requirements for the job'
        )

    def test_job_application_create_view(self):
        data = {
            'applicant': self.applicant.id,
            'job': self.job.id,
        }
        response = self.client.post('/api/job-applications/create', data, 
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobApplication.objects.count(), 1)
        self.assertEqual(JobApplication.objects.get().status, 'Applied')

    def test_job_application_list_view(self):
        JobApplication.objects.create(
            applicant=self.applicant,
            job=self.job,
        )
        
        # Retrieve the list of Job Applications
        response = self.client.get('/api/job-applications/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_job_application_update_view(self):
        job_application = JobApplication.objects.create(
            applicant=self.applicant,
            job=self.job,
        )

        # Update the status of the JobApplication
        data = {'status': 'Under Review'}
        response = self.client.put(f'/api/job-applications/{job_application.id}', data, 
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(JobApplication.objects.get().status, 'Under Review')

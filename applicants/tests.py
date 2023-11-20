import os
from django.db import IntegrityError
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from applicants.models import Applicant

# Create your tests here.
class ApplicantModelTest(TestCase):
    def test_applicant_creation(self):
        applicant = Applicant.objects.create(
            first_name="John",
            last_name="Doe",
            email="jdoe@gmail.com",
            phone_number="0789000122",
            resume="resumes/jdoe_resume.pdf"
        )
        self.assertEqual(applicant.email, "jdoe@gmail.com")

class ApplicantAPITest(APITestCase):
    def setUp(self):
        Applicant.objects.create(
            first_name="Mary",
            last_name="Jane",
            email="mjane@gmail.com",
            phone_number="0789555122",
            resume="resumes/mjane_resume.pdf"
        )

    def test_applicant_list_view(self):
        response = self.client.get('/api/applicants/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # def test_create_applicant_view(self):
    #     current_directory = os.path.dirname(os.path.abspath(__file__))
    #     file_path = os.path.join(current_directory, "test_resume/resume.txt")
        
    #     data = {
    #         "first_name": "Joshua",
    #         "last_name": "Jack",
    #         "email": "jjack@gmail.com",
    #         "phone_number": "0789333122",
    #     }
        
    #     with open(file_path, "rb") as file:
    #         files = {"resume": file}

    #         # Make a multipart request using requests.post
    #         response = self.client.post('/api/applicants/', format='multipart', data=data, files=files)
        
    #         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #         self.assertEqual(Applicant.objects.count(), 2)
        
    def test_duplicate_email_raises_integrity_error(self):
        with self.assertRaises(IntegrityError):
            Applicant.objects.create(
                first_name="Mercy",
                last_name="Jane",
                email="mjane@gmail.com",
                phone_number="0789456122",
                resume="resumes/mercyjane_resume.pdf"
            )

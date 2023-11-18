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
            resume_file_path="uploads/jdoe_resume.pdf"
        )
        self.assertEqual(applicant.email, "jdoe@gmail.com")

class ApplicantAPITest(APITestCase):
    def setUp(self):
        Applicant.objects.create(
            first_name="Mary",
            last_name="Jane",
            email="mjane@gmail.com",
            phone_number="0789555122",
            resume_file_path="uploads/mjane_resume.pdf"
        )

    def test_get_applicant_list(self):
        response = self.client.get('/api/applicants/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_applicant(self):
        data = {
            "first_name": "Joshua",
            "last_name": "Jack",
            "email": "jjack@gmail.com",
            "phone_number": "0789333122",
            "resume_file_path": "uploads/jjack_resume.pdf"
        }
        
        response = self.client.post('/api/applicants/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Applicant.objects.count(), 2)
        
    def test_duplicate_email_raises_integrity_error(self):
        with self.assertRaises(IntegrityError):
            Applicant.objects.create(
                first_name="Mercy",
                last_name="Jane",
                email="mjane@gmail.com",
                phone_number="0789456122",
                resume_file_path="uploads/mercyjane_resume.pdf"
            )

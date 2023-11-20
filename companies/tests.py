from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from companies.models import Company

# Create your tests here.
class CompanyAPITest(TestCase):
    def test_company_creation(self):
        company = Company.objects.create(
            name="Test Company",
            description="Description of the company",
            location="Test Location"
        )
        
        self.assertEqual(str(company), "Test Company")
        
class CompanyListCreateViewTest(APITestCase):

    def test_create_company_view(self):
        url = '/api/companies/'
        data = {
            "name": "Test Company",
            "description": "Description of the company",
            "location": "Test Location",
        }

        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)

        company = Company.objects.get()
        self.assertEqual(company.name, "Test Company")
        self.assertEqual(company.description, "Description of the company")
        self.assertEqual(company.location, "Test Location")

    def test_list_companies_view(self):
        Company.objects.create(name="Company A", description="Description A", location="Location A")
        Company.objects.create(name="Company B", description="Description B", location="Location B")

        url = '/api/companies/'

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


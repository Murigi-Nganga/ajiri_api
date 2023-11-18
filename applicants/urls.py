from django.urls import path

from applicants.views import ApplicantListCreateView

urlpatterns = [
    path('', ApplicantListCreateView.as_view(), name="applicant-list-create")
]
from django.urls import path

from .views import ApplicantJobApplicationListView, JobApplicationCreateView, JobApplicationListView, JobApplicationUpdateView

urlpatterns = [
    path('', JobApplicationListView.as_view(), name="job-application-list"),
    path('applicant/<int:applicant_id>', ApplicantJobApplicationListView.as_view(), name='applicant-job-applications'),
    # path('company/<str:company_name>', CompanyJobApplicationListView.as_view(), name='company-job-applications'),
    path('create', JobApplicationCreateView.as_view(), name="job-application-create"),
    path('<int:pk>', JobApplicationUpdateView.as_view(), name="job-application-update")
]

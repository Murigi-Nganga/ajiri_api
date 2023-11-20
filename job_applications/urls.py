from django.urls import path

from .views import JobApplicationCreateView, JobApplicationListView, JobApplicationUpdateView

urlpatterns = [
    path('', JobApplicationListView.as_view(), name="job-application-list"),
    path('create', JobApplicationCreateView.as_view(), name="job-application-create"),
    path('<int:pk>', JobApplicationUpdateView.as_view(), name="job-application-update")
]

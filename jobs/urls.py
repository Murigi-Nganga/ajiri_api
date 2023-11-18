from django.urls import path

from jobs.views import JobListCreateView


urlpatterns = [
    path('', JobListCreateView.as_view(), name="job-list-create")
]

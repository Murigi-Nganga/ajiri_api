from django.urls import path

from .views import JobApplicationListCreateView, JobApplicationUpdateView

urlpatterns = [
    path('', JobApplicationListCreateView.as_view(), name="job-application-list-create"),
    path('<int:pk>', JobApplicationUpdateView.as_view(), name="job-application-update")
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.studentsList, name="students"),
    path("schedule/", views.schedule, name="schedule"),
    path("studentdetails/<int:id>", views.studentsDetails, name="studentDetails"),
    path("testing/", views.testing, name="testing"),
]

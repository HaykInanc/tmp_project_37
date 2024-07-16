from django.urls import path
from .views import *

urlpatterns = [
    path("teachers/", TeacherListView.as_view(), name="teachers_list"),
    path("teacher/add/", TeacherCreateView.as_view()),
]

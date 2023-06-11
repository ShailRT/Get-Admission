from django.urls import path 
from . import views

urlpatterns = [
    path("<str:pk>/", views.course_detail, name="course-detail"),
]

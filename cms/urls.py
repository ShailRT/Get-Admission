from django.urls import path 
from . import views

urlpatterns = [
    path("<str:pk>/", views.college_detail, name="college-detail"),
    
]

from django.shortcuts import render
from .models import College

def college_detail(request, pk):
    college = College.objects.filter(slug=pk).first()

    context = {
        'college': college,
    }

    return render(request, 'college-detail.html', context)

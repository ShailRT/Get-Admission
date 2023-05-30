from django.shortcuts import render
from .models import College
from django.core.paginator import Paginator

from core.forms import CommentForm

def is_valid_param(param):
    return param != "" and param != None


def college_detail(request, pk):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save() 
    college = College.objects.filter(slug=pk).first()
    popular_colleges = College.objects.all()[:2]

    context = {
        'college': college,
        'popular_colleges': popular_colleges,
        'form': form,
    }

    return render(request, 'college-detail.html', context)

def college_list(request):
    college_objs = College.objects.all()
    search_include = request.GET.get('search_include')
    type_include = request.GET.get('type_include')
    state_include = request.GET.get('state_include')
    city_include = request.GET.get('city_include')

    if is_valid_param(search_include):
        college_objs = college_objs.filter(title__icontains=search_include)
    
    if is_valid_param(type_include):
        college_objs = college_objs.filter(institute_type__icontains=type_include)
    
    if is_valid_param(state_include):
        college_objs = college_objs.filter(location__icontains=state_include)
    
    if is_valid_param(city_include):
        college_objs = college_objs.filter(location__icontains=city_include)
    
    paginator = Paginator(college_objs, 6)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'colleges': page_obj,
        'search_include': search_include,
        'type_include': type_include,
        'state_include': state_include,
        'city_include': city_include,
    }

    return render(request, 'college-listing.html', context)

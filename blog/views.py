from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Blog
from core.forms import CommentForm

def blog_detail(request, pk):
    blog = Blog.objects.filter(slug=pk).first()
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'blog': blog,
        'form': form,
    }

    return render(request, 'blog-details.html', context)

def blog_listing(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page_number')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog-listing.html', context)
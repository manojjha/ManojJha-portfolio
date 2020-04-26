from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def all_blogs(request):
    blogs = Blog.objects.order_by('-created_on')[:3]

    paginator = Paginator(blogs, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})




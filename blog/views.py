from django.shortcuts import render
from .models import BlogList
from django.core.paginator import Paginator

# Create your views here.

def  blog_list(request):
    blog_list = BlogList.objects.all()
    recent_posts = BlogList.objects.order_by( '-pub_date' )[:3]
    paginator = Paginator(blog_list , 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'blogs':page_obj ,
            'recent_posts':recent_posts}
    return render(request , 'blog/blog_list.html' , context)


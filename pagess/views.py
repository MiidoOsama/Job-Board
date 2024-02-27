from django.shortcuts import render
from .models import Candidates
from django.core.paginator import Paginator
# Create your views here.

def candidates(request):
    mycand = Candidates.objects.all()
    #pagination
    paginator = Paginator(mycand , 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request , 'candidates/candidates.html' , {'candidates' : page_obj})




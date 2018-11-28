from django.shortcuts import render
from .models import Page

def Page_list(request):
    context = {
        "Page": Page.objects.all()
    }
    return render(request, 'list.html', context)

def Page_detail(request,page_id):
    context = {
        "Page": Page.objects.get(id=1),
    }
    return render(request, 'detail.html', context)
from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request,'test_temp/index.html')

def aboutpage(request):
    return render(request,'test_temp/about.html')

def contact(request):
    return render(request,'test_temp/contact.html')

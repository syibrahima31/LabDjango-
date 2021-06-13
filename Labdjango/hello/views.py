from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_django(request):
    return HttpResponse("Hello World!")

def test_django_1(request):
    return HttpResponse("Bonjour Mr SY")


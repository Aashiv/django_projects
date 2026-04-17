





from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('Hello World! This is Home Page.')
    return render(request,'home.html')

def about(request):
    # return HttpResponse("My About Page.")
    return render(request,'about.html')
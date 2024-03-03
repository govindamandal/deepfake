from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
      fullName: "Shubham Kshariya",
      age: 22,
      destination: "Software Engineer"
    }
    return render(request, 'index.html', context)
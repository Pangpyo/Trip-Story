from django.shortcuts import render

# Create your views here.

def inform(request):
  return render(request,'places/inform.html')
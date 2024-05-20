from django.shortcuts import render

def welcome(request):
    return render(request, 'map/index.html') 
# Create your views here.

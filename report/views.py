from django.shortcuts import render

def HomeView(request):
    return render(request, 'index.html')
# Create your views here.

from django.shortcuts import render

# Create your views here.

def drink_list(request):
    return render(request,'menu/index.html')
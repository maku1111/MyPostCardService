from django.shortcuts import render

# Create your views here.
def homeaction(request):
    return render(request,'Home.html')
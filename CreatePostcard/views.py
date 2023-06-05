from django.shortcuts import render

# Create your views here.
def createpostcardaction(request):
    return render(request,'Create_your_postcard.html')
